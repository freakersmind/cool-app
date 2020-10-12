#!/usr/bin/env bash
set -e
set -x

pycodestyle --count ./greeter
pylint greeter

set +e
py.test --cov=greeter --cov-report=html --cov-branch test/ --junitxml=test_results.xml "$@"
coverage xml
