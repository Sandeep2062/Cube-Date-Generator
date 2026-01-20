#!/bin/bash

# Quick Start Guide for Data Generator
# Run this file to start generating data

echo "=========================================="
echo "Data Generator for Weight & Strength"
echo "=========================================="
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 data_generator.py
elif command -v python &> /dev/null; then
    python data_generator.py
else
    echo "Error: Python not found!"
    echo "Please install Python 3.7 or higher"
    exit 1
fi
