#!/bin/bash

# Extract usernames from lines where a new user is added
grep 'new user' auth.log | awk -F'name=' '{print $2}' | cut -d',' -f1 | sort -u | paste -sd,

