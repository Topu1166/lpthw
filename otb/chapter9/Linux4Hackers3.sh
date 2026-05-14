#! /usr/bin/env bash 

echo "Enter the starting IP address: " 
read FirstIP 

echo "Enter the last octet of the last IP address: "
read LastOctetIP 

nmap -sV $FirstIP-$LastOctetIP -oG Linux4Hackers3_all > /dev/null

cat Linux4Hackers3_all | grep open > Linux4Hackers3_open 

cat Linux4Hackers3_open 
