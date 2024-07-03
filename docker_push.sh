#!/bin/bash

set -e

sudo docker login --username andrewjw --password $DOCKER_TOKEN

sudo docker buildx create --use

sudo docker buildx build --platform linux/amd64,linux/arm64 \
                         --build-arg VERSION=$TAG \
                         -t andrewjw/glowprom:$TAG \
                         -t andrewjw/glowprom:latest \
                         --push .
