#!/bin/bash
#-N to gen the key with empty pass phrase
KEY_FILENAME=$1
ssh-keygen -t rsa -b 4096 -f "$KEY_FILENAME" -N ""
