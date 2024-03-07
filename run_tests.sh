#!/bin/bash
PYTHON=python
export PYTHONPATH=.:./src

# if the first test fails then the whole script must fail 
$PYTHON src/beatbox/tests/test_beatbox.py &&
$PYTHON src/beatbox/tests/test_pythonClient.py
