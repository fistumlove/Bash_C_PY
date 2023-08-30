#include <stdio.h>
#include <math.h>
#include <string.h>
#include "t.h"
int main()
{
    z = x + y; printf("%d\n", z); z = x - y; printf("%d\n", z);
    z = x * y; printf("%d\n", z); z = x / y; printf("%d\n", z);

    printf("\nHello %s! Your gender is %s and you are %d years old!\n", name, sex, age);

    int len = strlen(name); printf("\nLength of your name = %d\n", len);
    int num = pow(8, 2); printf("Power of 8 = %d\n", num);

    int a = 6;
    printf("\nThe factorial of %d is equal to %d\n", a, f(a));

}