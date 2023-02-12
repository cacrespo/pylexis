# How to contribute to the project

Thank you very much for you interest in the project! :smile:


First, choose a issue (or create one with suggestions, ideas, tips...) and wait for the assignment.

Then clone the repository and work on the development branch. 

## Setup

We strongest suggest create a virtualenv, activate and install requirements.

    $ python3 -m venv env
    $ source env/bin/activate
    (env) $ pip install -r requirements-dev.txt

## Run tests

Get into the virtualenv, and:

    (env) $ python -m pytest tests/
