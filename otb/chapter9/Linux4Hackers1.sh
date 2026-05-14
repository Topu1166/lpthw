#! /usr/bin/env bash 
echo "Enter the starting IP address: "
read FirstIP

echo "Enter the last octet of the last IP address: " 
read  LastOctetIP

echo "Enter the port number you want to scan for: "
read Port 

nmap -sT $FirstIP-$LastOctetIP -p $Port -oG Linux4Hackers1_all > /dev/null 

cat Linux4Hackers1_all | grep open > Linux4Hackers1_open  

cat Linux4Hackers1_open  
