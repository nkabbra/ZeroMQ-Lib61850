cmake_minimum_required(VERSION 2.8.12)

project(zmq-iec61850)

set(gateway_SRCS
   gateway.c
)

IF(MSVC)
set_source_files_properties(${gateway_SRCS}
                                       PROPERTIES LANGUAGE CXX)
ENDIF(MSVC)

# Set the include directories of header files
include_directories(/usr/local/include/libiec61850)

add_executable(gateway
  ${gateway_SRCS}
)


set(client_sub_SRCS
   client_sub.c
)
IF(MSVC)
set_source_files_properties(${client_sub_SRCS}
                                       PROPERTIES LANGUAGE CXX)
ENDIF(MSVC)

add_executable(client_sub
  ${client_sub_SRCS}
)







target_link_libraries(gateway
    libiec61850.so
    libiec61850.a
    libhal.a
    libhal-shared.a
    pthread
    m
    czmq
    zmq
)


target_link_libraries(client_sub
    libiec61850.so
    libiec61850.a
    libhal.a
    libhal-shared.a
    pthread
    m
)