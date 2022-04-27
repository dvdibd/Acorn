#!/bin/bash
#! /usr/bin/env sh

echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################\n"
count=0 # number of test cases run so far

# Assume all `.in` and `.out` files are located in a separate `tests_e2e` directory

for test in tests_e2e/*.in; do
    name=$(basename $test .in)
    expected=tests_e2e/$name.out
    configFile=tests_e2e/$name.config

    # Change this command to run your program!
    # You will need to read the code here and figure out how to pass in your config yourself!
    
    python3 run.py $configFile < $test | diff - $expected || echo "Test $name: failed!\n"

    count=$((count+1))
done

echo "Finished running $count tests!"