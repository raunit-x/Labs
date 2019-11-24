#!/bin/bash

while IFS= read -r line; do
	for word in $line
	do 
		echo $word
	done
done < file.txt