#!/bin/bash

# Add all changes
git add .

# Get current date, day, and time
current_date=$(date +"%Y-%m-%d")
current_day=$(date +"%A")
current_time=$(date +"%H:%M")

# Create commit message
commit_message="Commit on $current_date $current_day at $current_time"

# Commit changes
git commit -m "$commit_message"

# Push to GitHub
git push -u origin main

echo "Changes have been pushed to GitHub successfully!"