/*
 * goose_subscriber_example.c
 *
 * This is an example for a standalone GOOSE subscriber
 *
 * Has to be started as root in Linux.
 */

#include <libiec61850/linked_list.h> /* for Thread_sleep() */
#include <libiec61850/hal_thread.h>
#include <libiec61850/goose_subscriber.h>
#include <libiec61850/goose_receiver.h>
#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
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
gooseListener(GooseSubscriber subscriber, void* parameter)
{
   
    int64_t elapsed_time = get_timestamp();
    printf(" received new GOOSE with SqNum: %i t: %"PRIi64" usec \n",GooseSubscriber_getSqNum(subscriber), elapsed_time);


    MmsValue* values = GooseSubscriber_getDataSetValues(subscriber);

}

int
main(int argc, char** argv)
{
    GooseReceiver receiver = GooseReceiver_create();
    freopen("./logs/log.csv", "w", stdout);


    if (argc > 1) {
        printf("Set interface id: %s\n", argv[1]);
        GooseReceiver_setInterfaceId(receiver, argv[1]);
    }
    else {
        printf("Using interface eth0\n");
        GooseReceiver_setInterfaceId(receiver, "eth0");
    }

    GooseSubscriber subscriber = GooseSubscriber_create("simpleIOGenericIO/LLN0$GO$gcbAnalogValues", NULL);

    uint8_t dstMac[6] = {0x01,0x0c,0xcd,0x01,0x00,0x01};
    GooseSubscriber_setDstMac(subscriber, dstMac);
    GooseSubscriber_setAppId(subscriber, 1000);

    GooseSubscriber_setListener(subscriber, gooseListener, NULL);

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

    GooseReceiver_stop(receiver);

    GooseReceiver_destroy(receiver);

    return 0;
}
