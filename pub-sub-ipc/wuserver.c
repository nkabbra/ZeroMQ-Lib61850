//  Weather update server
//  Binds PUB socket to tcp://*:5556
//  Publishes random weather updates

// gcc -o wuserver wuserver.c -lczmq -lzmq


#include "zhelpers.h"
#include <czmq.h>
#include <signal.h>
#include <unistd.h>
// docker volume create --name=ipc-shared-volume

// gcc -o wuserver wuserver.c -lczmq -lzmq

// docker run --rm -v ipc-shared-volume:/tmp zmq-pub


// Signal handler function
void handle_sigint(int sig) {
    printf("Caught SIGINT, exiting...\n");
    // Perform cleanup here
    exit(0);
}


int64_t get_timestamp() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return ((int64_t)tv.tv_sec) * 1000000 + (int64_t)tv.tv_usec;
}


int main (void)
{
    // Register the signal handler for SIGINT
    signal(SIGINT, handle_sigint);

    freopen("./logs/log.csv", "w", stdout);


    //  Prepare our context and publisher
    void *context = zmq_ctx_new ();
    void *publisher = zmq_socket (context, ZMQ_PUB);
    /*int rc = zmq_bind (publisher, "tcp://*:5556");*/
    int rc = zmq_bind (publisher, "ipc:///tmp/publisher");
    assert (rc == 0);

    int sqNum=0 ;

    //  Initialize random number generator
    srandom ((unsigned) time (NULL));
    while (1) {
        //  Get values that will fool the boss
        int temperature, relhumidity;
        temperature = randof (215) - 80;
        relhumidity = randof (50) + 10;

        sqNum = sqNum  +1 ;


        //  Send message to all subscribers
        char update [20];

        sprintf (update, "%d %d SqNum: %d", temperature, relhumidity, sqNum);
        fflush(stdout);
        int64_t send_time = get_timestamp();
        s_send (publisher, update);

        printf("Sent new weather update %s t: %" PRId64 " usec\n",update, send_time );
        fflush(stdout);
        usleep(10);
    }
    zmq_close (publisher);
    zmq_ctx_destroy (context);
    return 0;
}
