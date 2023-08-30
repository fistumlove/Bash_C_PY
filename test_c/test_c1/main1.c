#include <stdio.h>
#include <string.h>
#include <math.h>
#include "header1.h"

int main()
{
    x = 23; y = 17; z = x + y;
    printf("X + Y = %d\n", z);
    printf("Hello %s! You are a %s citizen and your current city is %s!\n", name, citizen, city);
    int len = strlen(name);
    printf("The lengeth of your name is : %d\n", len);
    int a = 6; int a1 = pow(6, 2);
    printf("The power of %d is equal to %d\n", a, a1);
    int a2 = 6;
    printf("The factorial of %d is equal to %d\n", a2, f(6));

}