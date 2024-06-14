#!/bin/bash

# Path to Pip executable
PIP_PATH="C:\Program Files\Python312\Scripts\pip.exe"

# Path to Python executable
PYTHON_PATH="C:\Program Files\Python312\python.exe"

# Install dependencies
"$PIP_PATH" install -r requirements.txt

# Run build commands
"$PYTHON_PATH" manage.py migrate
"$PYTHON_PATH" manage.py collectstatic --no-input
