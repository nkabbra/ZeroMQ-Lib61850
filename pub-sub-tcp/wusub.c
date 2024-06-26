//  Weather update client
//  Connects SUB socket to tcp://localhost:5556
//  Collects weather updates and finds avg temp in zipcode

// gcc -o wusub wusub.c -lczmq -lzmq

// docker run --rm -v ipc-shared-volume:/tmp zmq-sub

#include "zhelpers.h"
#include <czmq.h>
#include <zmq.h>
#include <string.h>
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/time.h>  // For gettimeofday

int64_t get_timestamp() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return ((int64_t)tv.tv_sec) * 1000000 + (int64_t)tv.tv_usec;
}

// Signal handler function
void handle_sigint(int sig) {
    printf("Caught SIGINT, exiting...\n");
    // Perform cleanup here
    exit(0);
}


int main (int argc, char *argv [])
{
    // Register the signal handler for SIGINT
    signal(SIGINT, handle_sigint);

    //  Socket to talk to server
    printf ("Collecting updates from zmq-iec61850 server...\n");
    void *context = zmq_ctx_new ();
    void *subscriber = zmq_socket (context, ZMQ_SUB);

    if (!subscriber) {
        perror("Error creating socket");
        zmq_ctx_destroy(context);
        return -1;
        }

    const char *server_ip = argv[1];
    char connection_string[256];
    snprintf(connection_string, sizeof(connection_string), "tcp://%s:5556", server_ip);

    printf("%s \n",connection_string);
    zmq_connect(subscriber, connection_string);

    // int rc = zmq_connect (subscriber, "tcp://localhost:5556");

    // Subscribe to zipcode, default is NYC, 10001
    zmq_setsockopt (subscriber, ZMQ_SUBSCRIBE, "", 0);
    int update_nbr;


    // freopen("logs/log.csv", "w",stdout);

    while(true){

        int64_t start_time = get_timestamp();

        //  Process 100 updates
       
        float total_value = 0;

        char *string = s_recv (subscriber);

        
        //  Calculate and report duration of batch
        int64_t end_time = get_timestamp();
        int64_t elapsed_time=  (int) (end_time - start_time);
        printf ("Received update with %s t: %" PRId64 " usec\n",string,end_time);
        printf ("Total elapsed time: %" PRId64 " usec\n",elapsed_time);
        free (string);

        
    }
  
    zmq_close (subscriber);
    zmq_ctx_destroy (context);
    return 0;
}
