#include <stdio.h>
#include <math.h>
#include <string.h>
#include "header.h"

int main()
{
    x; y; z;
    //z = x + y; z = x - y; z = x * y; z = x / y;
    printf("X plus Y = %d\n", x + y);
    printf("X plus Y = %d\n", x - y);
    printf("X plus Y = %d\n", x * y);
    printf("X plus Y = %d\n", x / y);
    printf("Hello %s! Your gender is %s and your grade is %s!\n", name, sex, grade);

    int len = strlen(name);
    printf("Length of name = %d\n", len);
    int x = pow(4, 2);
    printf("Power of x = %d\n", x);

    int n = 6;
    printf("Factorial of %d = %d\n", n, fact(6));
    
}