#! /bin/bash

echo "Welcome to the password generator script!"
read -p "Enter the length of the password to be generated: " length
read -p "Enter the number of passwords you want to generate: " num

for p in $(seq 1 $num);
do
    openssl rand -base64 48 | cut -c1-$length
done
