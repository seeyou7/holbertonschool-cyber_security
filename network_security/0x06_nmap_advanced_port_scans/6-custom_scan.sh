#!/bin/bash
sudo nmap -p $2 --scanflags SYNFINACK  $1 -oN custom_scan.txt
