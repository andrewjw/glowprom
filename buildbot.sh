#!/bin/bash

set -e

export

pip install -r requirements.txt

./code_style.sh
./run_tests.sh

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" == "master" ]]; then
  coveralls
  semantic-release publish
fi

#docker_push.sh
