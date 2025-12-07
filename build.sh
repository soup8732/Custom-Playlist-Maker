#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements-web.txt

echo "Installing ffmpeg..."
# Render uses Ubuntu, so we can use apt-get
apt-get update
apt-get install -y ffmpeg

echo "Build complete!"
