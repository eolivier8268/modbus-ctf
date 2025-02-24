#!/bin/bash
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

if ! systemctl is-active --quiet docker; then
    echo "Docker is not running. Please start Docker and try again."
    exit 1
fi

if ! ping -c 1 8.8.8.8 &> /dev/null; then
    echo "No internet access. Please check your network connection and try again."
    exit 1
fi

if ! ping -c 1 google.com &> /dev/null; then
    echo "No internet access. Please check your network connection and try again."
    exit 1
fi

echo "System check passed. You can deploy challenges with the docker-env script"
echo "Usage: ./docker-env.sh {up|down} {challenge_number}"
echo "Flag: DELOGRAND{setup_complete}"