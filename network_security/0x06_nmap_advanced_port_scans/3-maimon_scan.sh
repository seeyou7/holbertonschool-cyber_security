#!/bin/bash
sudo nmap -sM  -vv -p 80,443,23,22,21 $1
