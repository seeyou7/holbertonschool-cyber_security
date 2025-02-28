#!/bin/bash
sudo map --script ssl-enum-ciphers -p 443 "$1"
