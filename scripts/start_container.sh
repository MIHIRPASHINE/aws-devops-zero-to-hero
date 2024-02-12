#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull mihirpashine/simple-python-flask-app

# Run the Docker image as a container
docker run -d -p 5000:9090 mihirpashine/simple-python-flask-app

