#!/bin/bash

set -e

mypy bin/glowprom glowprom/ tests/

black .
