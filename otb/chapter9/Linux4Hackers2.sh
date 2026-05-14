#! /usr/bin/env bash 

echo "Enter the IP address: "
read IP 

nmap -sV $IP -oG Linux4Hackers2_all > /dev/null

cat Linux4Hackers2_all | grep open > Linux4Hackers2_open 

cat Linux4Hackers2_open 
