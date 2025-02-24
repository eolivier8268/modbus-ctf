#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 {up|down} {challenge_number}"
    exit 1
fi


if [ "$1" == "up" ]; then
    if [ $2 == 6 ]; then
        docker network create --driver bridge --subnet 172.18.6.0/24 chall6_net
        cd /home/emile/training/modbus-ctf/6\ -\ spoofIt
        docker build -f Dockerfile.server -t 6_modbus_server .
        docker run -d --name 6_modbus_server --network chall6_net 6_modbus_server
        docker build -f Dockerfile.client -t 6_modbus_client .
        docker run -d --name 6_modbus_client --network chall6_net 6_modbus_client
        docker build -f Dockerfile.webapp -t 6_modbus_webapp .
        docker run -d --name 6_modbus_webapp --network chall6_net 6_modbus_webapp
    elif [ $2 == 7 ]; then 
        docker network create --driver bridge --subnet 172.18.7.0/24 chall7_net
        cd /home/emile/training/modbus-ctf/7\ -\ Denied
        docker build -f Dockerfile.server -t 7_modbus_server .
        docker run -d --name 7_modbus_server --network chall7_net 7_modbus_server
        docker build -f Dockerfile.client -t 7_modbus_client .
        docker run -d --name 7_modbus_client --network chall7_net 7_modbus_client
        docker build -f Dockerfile.webapp -t 7_modbus_webapp .
        docker run -d --name 7_modbus_webapp --network chall7_net 7_modbus_webapp
    else
        echo "Usage: $0 {up|down} {2}"
    fi
elif [ "$1" == "down" ]; then
    if [ $2 == 6 ]; then
        docker container stop 6_modbus_server 6_modbus_client 6_modbus_webapp
        docker container rm 6_modbus_server 6_modbus_client 6_modbus_webapp
        docker image rm 6_modbus_server 6_modbus_client 6_modbus_webapp
    elif [ $2 == 7 ]; then
        docker container stop 7_modbus_server 7_modbus_client 7_modbus_webapp
        docker container rm 7_modbus_server 7_modbus_client 7_modbus_webapp
        docker image rm 7_modbus_server 7_modbus_client 7_modbus_webapp
    else 
        echo "Usage: $0 {up|down} {challenge_number}"
        exit 1
    fi
else
    echo "Usage: $0 {up|down} {challenge_number}"
    exit 1
fi