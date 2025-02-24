#!/bin/bash
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 {up|down} {challenge_number}"
    exit 1
fi


if [ "$1" == "up" ]; then
    if [ $2 == 1 ]; then
        docker network create --driver bridge --subnet 172.18.1.0/24 chall1_net
        cd ./1\ -\ My\ First\ Modbus
        docker build -f Dockerfile -t 1_server .
        docker run -d --name 1_server --network chall1_net 1_server
    elif [ $2 == 2 ]; then
        docker network create --driver bridge --subnet 172.18.2.0/24 chall2_net
        cd ./2\ -\ What\'s\ a\ Coil
        docker build -f Dockerfile -t 2_server .
        docker run -d --name 2_server --network chall2_net 2_server
    elif [ $2 == 3 ]; then
        docker network create --driver bridge --subnet 172.18.3.0/24 chall3_net
        cd ./3\ -\ Anyone\ Can\ Write
        docker build -f Dockerfile -t 3_server .
        docker run -d --name 3_server --network chall3_net 3_server
    elif [ $2 == 4 ]; then
        docker network create --driver bridge --subnet 172.18.4.0/24 chall4_net
        cd "./4 - What's this device"
        docker build -f Dockerfile -t 4_server .
        docker run -d --name 4_server --network chall4_net 4_server
    elif [ $2 == 6 ]; then
        docker network create --driver bridge --subnet 172.18.6.0/24 chall6_net
        cd "./6 - Watch and Learn"
        docker build -f Dockerfile.server -t 6_modbus_server .
        docker run -d --name 6_modbus_server --network chall6_net 6_modbus_server
        docker build -f Dockerfile.client -t 6_modbus_client .
        docker run -d --name 6_modbus_client --network chall6_net 6_modbus_client
        docker build -f Dockerfile.webapp -t 6_modbus_webapp .
        docker run -d --name 6_modbus_webapp --network chall6_net 6_modbus_webapp
    elif [ $2 == 7 ]; then 
        docker network create --driver bridge --subnet 172.18.7.0/24 chall7_net
        cd ./7\ -\ Denied
        docker build -f Dockerfile.server -t 7_modbus_server .
        docker run -d --name 7_modbus_server --network chall7_net 7_modbus_server
        docker build -f Dockerfile.client -t 7_modbus_client .
        docker run -d --name 7_modbus_client --network chall7_net 7_modbus_client
        docker build -f Dockerfile.webapp -t 7_modbus_webapp .
        docker run -d --name 7_modbus_webapp --network chall7_net 7_modbus_webapp
    elif [ $2 == 8 ]; then 
        docker network create --driver bridge --subnet 172.18.8.0/24 chall8_net
        cd ./8\ -\ Denied\ II
        docker build -f Dockerfile.server -t 8_modbus_server .
        docker run -d --name 8_modbus_server --network chall8_net 8_modbus_server
        docker build -f Dockerfile.client -t 8_modbus_client .
        docker run -d --name 8_modbus_client --network chall8_net 8_modbus_client
        docker build -f Dockerfile.webapp -t 8_modbus_webapp .
        docker run -d --name 8_modbus_webapp --network chall8_net 8_modbus_webapp
    else
        echo "Usage: $0 {up|down} {2}"
    fi
elif [ "$1" == "down" ]; then
    if [ $2 == 1 ]; then
        docker container stop 1_server
        docker container rm 1_server
        docker image rm 1_server
    elif [ $2 == 2 ]; then
        docker container stop 2_server
        docker container rm 2_server
        docker image rm 2_server
    elif [ $2 == 3 ]; then
        docker container stop 3_server
        docker container rm 3_server
        docker image rm 3_server
    elif [ $2 == 4 ]; then
        docker container stop 4_server
        docker container rm 4_server
        docker image rm 4_server
    elif [ $2 == 6 ]; then
        docker container stop 6_modbus_server 6_modbus_client 6_modbus_webapp
        docker container rm 6_modbus_server 6_modbus_client 6_modbus_webapp
        docker image rm 6_modbus_server 6_modbus_client 6_modbus_webapp
    elif [ $2 == 7 ]; then
        docker container stop 7_modbus_server 7_modbus_client 7_modbus_webapp
        docker container rm 7_modbus_server 7_modbus_client 7_modbus_webapp
        docker image rm 7_modbus_server 7_modbus_client 7_modbus_webapp
    elif [ $2 == 8 ]; then
        docker container stop 8_modbus_server 8_modbus_client 8_modbus_webapp
        docker container rm 8_modbus_server 8_modbus_client 8_modbus_webapp
        docker image rm 8_modbus_server 8_modbus_client 8_modbus_webapp
    else 
        echo "Usage: $0 {up|down} {challenge_number}"
        exit 1
    fi
else
    echo "Usage: $0 {up|down} {challenge_number}"
    exit 1
fi
