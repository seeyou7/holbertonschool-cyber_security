#!/bin/bash
whois "$1" | awk -F': ' '
/^(Registrant|Admin|Tech)/ {
    gsub(": ", ",");  # to Replace ": " with ","
    gsub(", ", ",");  # to Remove spaces after commas
    print $1 "," $2}' > "$1.csv"
