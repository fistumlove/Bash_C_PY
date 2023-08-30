#!/usr/bin/bash
echo 'hi!'; echo 'hi!'; echo 'hi!';
a=0; while [ $a -le 2 ]; do echo 'hey!'; ((a++)); done;
b=0; until [ $b -ge 3 ]; do echo 'hello'; ((b++)); done; 
for c in c [0..2 ]
do
    echo 'selam!';
done