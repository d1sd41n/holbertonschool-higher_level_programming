#!/bin/bash
#  ends a JSON POST request to a URL
curl -Hs "Content-Type: application/json" -d @"$2" "$1"
