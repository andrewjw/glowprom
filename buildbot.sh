#!/bin/bash

set -e

python3.8 -m venv venv-3.8

. venv-3.8/bin/activate

pip3 install -r requirements.txt
./run_tests.sh
./code_style.sh

deactivate

python3.9 -m venv venv-3.9

. venv-3.9/bin/activate

pip3 install -r requirements.txt

./run_tests.sh
./code_style.sh

deactivate

python3.10 -m venv venv-3.10

. venv-3.10/bin/activate

pip3 install -r requirements.txt

./run_tests.sh
./code_style.sh

deactivate

python3.11 -m venv venv-3.11

. venv-3.11/bin/activate

pip3 install -r requirements.txt

./run_tests.sh
./code_style.sh

BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Building branch $BRANCH"
if [[ "$BRANCH" == "master" ]]; then
  COVERALLS_REPO_TOKEN=$GLOWPROM_COVERALLS_REPO_TOKEN coveralls
  semantic-release publish
fi
if [[ ${BRANCH:0:7} == "heads/v" ]]; then
    TAG=${BRANCH:7} ./docker_push.sh
fi
