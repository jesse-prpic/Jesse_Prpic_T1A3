#!/bin/bash
python -m venv venv

# Activating the virtual environemnt
source venv/bin/activate

# Install the depencenies from requirements.txt
pip install -r requirements.txt

# Run the main application python src/
deactivate