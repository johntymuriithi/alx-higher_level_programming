#!/bin/bash
# we printing out the response header
curl -sI "$1" | grep -E 'Content-(Type|Length)'
