# Django Descriptors

This sample project is the companion of a [blog
post](http://kevinastone.github.io/django-model-descriptors.html) on patterns
for building better models and fields using Descriptors.

## Setup

You're encouraged to setup a `virtualenv` to work in prior to configuring the
dependencies.

1. Install Python Requirements

        pip install -r dev-requirements.txt

2. Setup the Database

        ./manage.py syncdb

3. Load the models

        ./manage.py shell_plus
