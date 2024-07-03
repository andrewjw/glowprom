#!/bin/bash

set -e

sudo docker login --username andrewjw --password $DOCKER_TOKEN

sudo docker buildx --use

sudo docker build --platform linux/amd64,linux/arm64 \
                  --build-arg VERSION=$TAG \
                  -t andrewjw/glowprom:$TAG \
                  -t andrewjw/glowprom:latest .

sudo docker push andrewjw/glowprom:$TAG

sudo docker push andrewjw/glowprom:latest
