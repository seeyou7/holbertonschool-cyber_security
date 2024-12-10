#!/bin/bash
whois "$1" | awk -F': ' '/^(Registrant|Admin|Tech)/ {gsub(": ", ","); gsub(", ", ","); print $1 "," $2}' > "$1.csv"

