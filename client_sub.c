/*
 * client_example1.c
 *
 * This example is intended to be used with server_example_basic_io or server_example_goose.
 */

#include <libiec61850/iec61850_client.h>
#include <inttypes.h>  // Include for PRIi64
#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>  // For gettimeofday
#include <string.h>
#include <signal.h>
#include <stdint.h>
#include <libiec61850/hal_thread.h> /* for Thread_sleep() */


int64_t get_timestamp() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return ((int64_t)tv.tv_sec) * 1000000 + (int64_t)tv.tv_usec;
}



int main(int argc, char** argv) {

    char* hostname;
    int tcpPort = 102;
    const char* localIp = NULL;
    int localTcpPort = -1;
    

    if (argc > 1)
        hostname = argv[1];
    else
        hostname = "localhost";

    if (argc > 2)
        tcpPort = atoi(argv[2]);

    if (argc > 3)
        localIp = argv[3];

    if (argc > 4)
        localTcpPort = atoi(argv[4]);

    IedClientError error;

    IedConnection con = IedConnection_create();


    IedConnection_connect(con, &error, hostname, tcpPort);
    printf("Connecting to %s:%i\n", hostname, tcpPort);
    printf("Connected\n");

    int update_nbr;

    // Open a file in write mode
    FILE *logFile = fopen("./logs/log.csv", "w");
    if (logFile == NULL) {
        perror("Error opening log file");
        return 1;
    }

    while (1 && error == IED_ERROR_OK)
    {

        int64_t start_time = get_timestamp();

        //  Process 100 updates
       
        float total_value = 0;
        for (update_nbr = 0; update_nbr < 10 ; update_nbr++) {

            /* read an analog measurement value from server */
            MmsValue* value = IedConnection_readObject(con, &error, "simpleIOGenericIO/GGIO1.AnIn1.mag.f", IEC61850_FC_MX);

            if (value != NULL)
            {
                if (MmsValue_getType(value) == MMS_FLOAT) {
                    float fval = MmsValue_toFloat(value);
                    printf("read float value: %f\n", fval);
                    total_value += fval;

                }
                else if (MmsValue_getType(value) == MMS_DATA_ACCESS_ERROR) {
                    printf("Failed to read value (error code: %i)\n", MmsValue_getDataAccessError(value));
                }

                MmsValue_delete(value);
            }
        }
        float average_value = (float)(total_value / update_nbr);
        printf ("Average value was total %f %f\n", total_value,average_value);

        //  Calculate and report duration of batch
        int64_t end_time = get_timestamp();
        int64_t elapsed_time=  (int) (end_time - start_time);

        printf ("Total elapsed time: %"PRIi64" usec\n",elapsed_time);


        // Write the values to the log file in CSV format
        fprintf(logFile, "%f,%f, %" PRIi64" \n", total_value, average_value,elapsed_time);

       
    }

    // Close the log file
    fclose(logFile);
    IedConnection_destroy(con);

    return 0;
}
