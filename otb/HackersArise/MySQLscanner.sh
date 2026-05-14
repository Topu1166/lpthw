#! /usr/bin/env bash 

#This script is designed to find hosts with MySQL installed 

nmap -sT 192.168.1.105/24 -p 3306 -oG MySQLscan 2>/dev/null

cat MySQLscan | grep open > MySQLscan2 

cat MySQLscan2

