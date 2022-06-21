#!/bin/bash

echo "Enter the Net Address (First 3 Octects) (IE xx.xx.xx): "
read net

echo "Enter starting host address (IE xxx): "
read start

echo "Enter the ending host address (IE xxx): "
read end

echo "Enter the ports you wish to scan. (Space in between port numbers) (IE 21-23 80): "
read ports

for (( i=$start; $i<=$end; i++))
do 
	nc -nvzw1 $net.$i $ports 2>&1 | grep open
done
