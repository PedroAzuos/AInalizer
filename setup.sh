#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Please install Python3 first."
    exit
fi

# Create virtual environment
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Load environment variables (API keys, etc.)
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Development environment set up and ready!"
