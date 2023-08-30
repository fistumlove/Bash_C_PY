#!/usr/bin/env bash

echo 'Hi!'; echo 'Hi!'; echo 'Hi!';
a=0; while [ $a -le 2 ]; do echo 'Hey!'; ((a++)); done;
a=0; until [ $a -ge 3 ]; do echo 'Hello!'; ((a++)); done;
for a in a [0..3 ]
do
    echo 'Selam!';
done


#!/usr/bin/env bash
echo 'Hello Fistum!';

i=0; while [ $i -le 2 ]; do echo 'I am proud of you!'; ((i++)); done

i=0; until [ $i -ge 3 ]; do echo 'Just dream big dude!'; ((i++)); done


for i in [ 0..2 ]
do
    echo 'You are wonderfull!'
done
