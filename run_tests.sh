#!/bin/bash

coverage run test.py

let R=$?

coverage report

coverage html

exit $R
