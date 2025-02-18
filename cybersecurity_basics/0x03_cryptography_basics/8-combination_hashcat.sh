#!/bin/bash
hashcat -m 0 hash.txt "$1" "$2"
