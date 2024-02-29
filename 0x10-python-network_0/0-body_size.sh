#!/bin/bash
# we printing out the response header
curl -s -w "\n${size_download}" | tail -n 1
