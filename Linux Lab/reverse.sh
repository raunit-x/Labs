#!/bin/bash

read -p "ENTER THE STRING TO BE REVERSED: " string
len=${#string}
reversed=""
for((i=$((len - 1)); i >= 0; --i))
do
	reversed="${reversed}${string:$i:1}"
done

echo "REVERSED STRING: ${reversed}"
