#!/bin/bash

test_file () {
    FILE=~/Desktop/Courses
    echo "File: "$FILE""
    if [ -e "$FILE" ]; then
        if [ -f "$FILE" ]; then
        	echo "$FILE is a regular file."
        fi
        if [ -d "$FILE" ]; then
        	echo "$FILE is a directory."
        fi
        if [ -r "$FILE" ]; then
            echo "$FILE is readable."
        fi
        if [ -w "$FILE" ]; then
            echo "$FILE is writable."
        fi
        if [ -x "$FILE" ]; then
            echo "$FILE is executable/searchable."
        fi 
    else
        echo "$FILE does not exist"
        return 1
    fi
}

test_file
