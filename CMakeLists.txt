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




set(gateway-gse_SRCS
   gateway-gse.c
)

IF(MSVC)
set_source_files_properties(${gateway-gse_SRCS}
                                       PROPERTIES LANGUAGE CXX)
ENDIF(MSVC)

# Set the include directories of header files
include_directories(/usr/local/include/libiec61850)

add_executable(gateway-gse
  ${gateway-gse_SRCS}
)



set(gateway-ipc-gse_SRCS
   gateway-ipc-gse.c
)

IF(MSVC)
set_source_files_properties(${gateway-ipc-gse_SRCS}
                                       PROPERTIES LANGUAGE CXX)
ENDIF(MSVC)

# Set the include directories of header files
include_directories(/usr/local/include/libiec61850)

add_executable(gateway-ipc-gse
  ${gateway-ipc-gse_SRCS}
)






# Set the include directories of header files
include_directories(/usr/local/include/libiec61850)
include_directories(
   .
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



target_link_libraries(gateway-gse
    libiec61850.so
    libiec61850.a
    libhal.a
    libhal-shared.a
    pthread
    m
    czmq
    zmq
)



target_link_libraries(gateway-ipc-gse
    libiec61850.so
    libiec61850.a
    libhal.a
    libhal-shared.a
    pthread
    m
    czmq
    zmq
)
