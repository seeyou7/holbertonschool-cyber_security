#!/bin/bash

grep -i "accepted password" auth.log | awk '{print $(NF-3)}' | sort -u | wc -l
