#!/bin/bash

# Vehicle Rental System - Unix/Linux/Mac Startup Script
# This script sets up and runs the Flask application

echo "╔════════════════════════════════════════════════════════╗"
echo "║     Vehicle Rental System - Phase 1 Implementation     ║"
echo "║              Unix/Linux/Mac Startup Script             ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 is not installed"
    echo "  Please install Python 3.9+ from https://python.org"
    exit 1
fi

echo "✓ Python found"
python3 --version
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install/update dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Run the Flask app
echo "Starting Flask application..."
echo ""
python3 app.py
