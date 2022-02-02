#!/bin/bash

# Loop through all child PIDs of steamlink.sh and kill.
while IFS= read -r pid 
do
    pkill -TERM -P $pid 
done <<< $(pgrep -x steamlink.sh)