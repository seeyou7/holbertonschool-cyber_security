#!/bin/bash
PASSWORD=$(cat /dev/urandom | tr -dc '[:alnum:]' | fold -w $1 | head -1)
echo $PASSWORD
