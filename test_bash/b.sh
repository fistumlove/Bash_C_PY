#!/usr/bin/env bash

echo 'Hi!'; echo 'Hi!'; echo 'Hi!';
x=0; while [ $x -le 2 ]; do echo 'Hey!'; ((x++)); done;
y=0; until [ $y -ge 3 ]; do echo 'Hello!'; ((y++)); done;
for z in z[ 0..3 ]:
do
    echo 'Selam!';
done


