#!/bin/bash
# we printing out the response header
curl -s "$1" | wc -c
