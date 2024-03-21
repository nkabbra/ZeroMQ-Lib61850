//  Weather update server
//  Binds PUB socket to tcp://*:5556
//  Publishes random weather updates

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
int main (void)
{
    //  Prepare our context and publisher
    void *context = zmq_ctx_new ();
    void *publisher = zmq_socket (context, ZMQ_PUB);
    int rc = zmq_bind (publisher, "tcp://*:5556");
    assert (rc == 0);
    freopen("logs/log.csv", "w",stdout);

    int SqNum=0;
    //  Initialize random number generator
    srandom ((unsigned) time (NULL));
    while (1) {
        //  Get values that will fool the boss
        int temperature;
        SqNum     = SqNum +1;
        temperature = randof (215) - 80;

        //  Send message to all subscribers
        char update [20];
        sprintf (update, "%d SqNum: %d",temperature, SqNum);
        int64_t send_time = get_timestamp();

        printf ("Sent update with SqNum: %d t: %" PRId64 " usec\n",SqNum,send_time);

        s_send (publisher, update);
    }
    zmq_close (publisher);
    zmq_ctx_destroy (context);
    return 0;
}
