#!/bin/bash

function gcd
{
	m=$1
	n=$2
	if [ $n -eq 0 -a $m -eq 0 ]; then
    	exit 1
    elif [ $m -eq 0 ]; then
    	return $n
    elif [ $n -eq 0 ]; then
    	return $m
  	fi
  	gcd $(( $n % $m )) $m
}


read -p "Enter two numbers for gcd: " num1 num2
gcd $num1 $num2
echo "GCD OF ${num1} and ${num2}: $?"
