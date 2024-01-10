#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <zmq.h>

#include "zhelpers.h"
#include <czmq.h>
#include <signal.h>

#include <libiec61850/iec61850_client.h>
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */

#include <stdint.h>
#include <sys/time.h>  // For gettimeofday

int64_t get_timestamp() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return ((int64_t)tv.tv_sec) * 1000000 + (int64_t)tv.tv_usec;
}

// ZeroMQ Constants
#define ZMQ_PUB_PORT "tcp://*:5556"

// IEC 61850 Constants
#define IED_IP "192.168.1.1"
#define IED_PORT 102


// Signal handler function
void handle_sigint(int sig) {
    printf("Caught SIGINT, exiting...\n");
    // Perform cleanup here
    exit(0);
}




void initialize_zmq_publisher(void** zmq_context, void** zmq_publisher) {
    *zmq_context = zmq_ctx_new();
    *zmq_publisher = zmq_socket(*zmq_context, ZMQ_PUB);
    zmq_bind(*zmq_publisher, ZMQ_PUB_PORT);
}


void cleanup(void* zmq_context) {
    zmq_ctx_destroy(zmq_context);

}

int main(int argc, char** argv) {
    void* zmq_context;
    void* zmq_publisher;
    IedConnection* ied_connection;
    char* hostname;
    int tcpPort = 102;
    const char* localIp = NULL;
    int localTcpPort = -1;
    IedClientError error;

    if (argc > 1)
        hostname = argv[1];
    else
        hostname = "localhost";

    if (argc > 2)
        tcpPort = atoi(argv[2]);

     // Register the signal handler for SIGINT
    signal(SIGINT, handle_sigint);


    IedConnection con = IedConnection_create();

    initialize_zmq_publisher(&zmq_context, &zmq_publisher);
 
    IedConnection_connect(con, &error, hostname, tcpPort);
    printf("Connecting to %s:%i\n", hostname, tcpPort);
    printf("Connected\n");


    while (1 && error == IED_ERROR_OK) {
        // Receive data from IEC 61850
        int64_t start_time = get_timestamp();

        
         /* read an analog measurement value from server */
        MmsValue* value = IedConnection_readObject(con, &error, "simpleIOGenericIO/GGIO1.AnIn1.mag.f", IEC61850_FC_MX);

        //  Calculate and report duration of batch
        int64_t end_time = get_timestamp();
        int64_t elapsed_time=  (int) (end_time - start_time);
        printf ("Total elapsed time: %" PRId64 " usec\n",elapsed_time);

        if (value != NULL)
        {
            if (MmsValue_getType(value) == MMS_FLOAT) {
                float fval = MmsValue_toFloat(value);
                printf("read iec61850 mms float value: %f\n", fval);

                  //  Send message to all subscribers
                char update [20];
                sprintf (update, "%f",fval);
                s_send (zmq_publisher, update);
                printf("Sent new update from zmq %s \n",update );

            }
            else if (MmsValue_getType(value) == MMS_DATA_ACCESS_ERROR) {
                printf("Failed to read value (error code: %i)\n", MmsValue_getDataAccessError(value));
            }

            
        }

      


        MmsValue_delete(value);

    }

    cleanup(zmq_context);
    zmq_close (zmq_publisher);
    IedConnection_close(con);
    IedConnection_destroy(con);
    return 0;
}
