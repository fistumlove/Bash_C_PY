#!/usr/bin/env bash

echo 'Hi!'; echo 'Hi!'; echo 'Hi!';
a=0; while [ $a -le 2 ]; do echo 'Hey!'; ((a++)); done;
a=0; until [ $a -ge 3 ]; do echo 'Hello!'; ((a++)); done;
for a in a [0..3 ]
do
    echo 'Selam!';
done
