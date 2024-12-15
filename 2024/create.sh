#!/bin/bash
# Takes arguments
#   $1 = day number 
#   $2 = sample test value

printf -v day "%02d" $1

asg1=$day/$day-1.py
asg2=$day/$day-2.py

echo "Creating directory for Day $day"
mkdir $day
cp template.py $asg1
cp template.py $asg2

touch $day/sample.txt
touch $day/input.txt
# curl -o $day/input.txt https://adventofcode.com/2024/day/$1/input

# sampleLine="result = work(\"$day/sample.txt\")"
# inputLine="#result = work(\"$day/input.txt\")"
# printLine="println(\"Result: \", result)"

# echo $sampleLine >> $asg1
# echo "DEBUG=false" >> $asg1
# echo $inputLine >> $asg1
# echo $printLine >> $asg1

# echo $sampleLine >> $asg2
# echo "DEBUG=false" >> $asg2
# echo $inputLine >> $asg2
# echo $printLine >> $asg2

# if [ ! -z "$2" ] 
#   then
#     echo "@test result == $2" >> $asg1
#     echo "@test result == $2 skip=true" >> $asg2
# fi