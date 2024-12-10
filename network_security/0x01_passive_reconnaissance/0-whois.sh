#!/bin/bash
whois $1 | awk -F ',' '/^(Registrant|Admin|Tech)/{gsub(":", ","); gsub(" ", "$"); print$0 "$"}' > $1.csv
