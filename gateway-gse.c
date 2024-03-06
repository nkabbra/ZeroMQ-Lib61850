#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <zmq.h>

#include "zhelpers.h"
#include <czmq.h>
#include <signal.h>

#include <libiec61850/hal_thread.h> /* for Thread_sleep() */
#include <libiec61850/goose_subscriber.h>
#include <libiec61850/goose_receiver.h>
#include <libiec61850/linked_list.h>
#include <stdint.h>
#include <sys/time.h>  // For gettimeofday
#include <inttypes.h>

static int running = 1;

static void
sigint_handler(int signalId)
{
    running = 0;
}

int64_t get_timestamp() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return ((int64_t)tv.tv_sec) * 1000000 + (int64_t)tv.tv_usec;
}


static void
gooseListener(GooseSubscriber subscriber, void* zmq_publisher)
{
   
    int64_t elapsed_time1 = get_timestamp();
    printf("  elapsed time-g: %"PRIi64" usec\n",elapsed_time1);
    MmsValue* ds_values = GooseSubscriber_getDataSetValues(subscriber);

    char buffer[1024];

    MmsValue_printToBuffer(ds_values, buffer, 1024);


    s_send (zmq_publisher, buffer);
    printf("  Sent new update from zmq SqNum: %d t: %"PRIi64" usec\n",   GooseSubscriber_getSqNum(subscriber),elapsed_time1 );

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

    float firstValue;

void cleanup(void* zmq_context) {
    zmq_ctx_destroy(zmq_context);

}

int main(int argc, char** argv) {
    void* zmq_context;
    void* zmq_publisher;
    char* hostname;
    int tcpPort = 102;
    const char* localIp = NULL;
    int localTcpPort = -1;

    GooseReceiver receiver = GooseReceiver_create();


    if (argc > 1)
        {  printf("Set interface id: %s\n", argv[1]);
        GooseReceiver_setInterfaceId(receiver, argv[1]);
        }
    else
       {printf("Using interface eth0\n");
        GooseReceiver_setInterfaceId(receiver, "eth0");
        }

    if (argc > 2)
        tcpPort = atoi(argv[2]);



    initialize_zmq_publisher(&zmq_context, &zmq_publisher);


    GooseSubscriber subscriber = GooseSubscriber_create("simpleIOGenericIO/LLN0$GO$gcbAnalogValues", NULL);

    uint8_t dstMac[6] = {0x01,0x0c,0xcd,0x01,0x00,0x01};
    GooseSubscriber_setDstMac(subscriber, dstMac);
    GooseSubscriber_setAppId(subscriber, 1000);

    GooseSubscriber_setListener(subscriber, gooseListener, zmq_publisher);

    GooseReceiver_addSubscriber(receiver, subscriber);

    GooseReceiver_start(receiver);

    if (GooseReceiver_isRunning(receiver)) {
        signal(SIGINT, sigint_handler);

        while (running) {
            Thread_sleep(0.01);
           
        }
    }
    else {
        printf("Failed to start GOOSE subscriber. Reason can be that the Ethernet interface doesn't exist or root permission are required.\n");
    }

 


    cleanup(zmq_context);
    zmq_close (zmq_publisher);
    GooseReceiver_stop(receiver);
    GooseReceiver_destroy(receiver);
 
    return 0;
}
