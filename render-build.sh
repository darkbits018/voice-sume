#!/usr/bin/env bash

# Update package list
apt-get update -y

# Install system-level dependencies
apt-get install -y portaudio19-dev python3-pyaudio

# Upgrade pip to the latest version
pip install --upgrade pip

# Install Python dependencies from requirements.txt
pip install -r requirements.txt
