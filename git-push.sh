#!/bin/bash

# Check if a commit message is supplied
if [ -z "$1" ]; then
  echo "Error: No commit message supplied."
  echo "Usage: ./git_push.sh <commit-message>"
  exit 1
fi

# Perform git add, commit, and push
git add .
git commit -m "$1"
git push
