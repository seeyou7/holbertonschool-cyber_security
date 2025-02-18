#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-SHA256 $1
