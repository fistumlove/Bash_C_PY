#include <stdio.h>
#include <string.h>
#include <math.h>
#include "main.h"

int main()
{
    x = 20; y = 8; 
    z = x + y; printf("%d\t", z);
    z = x - y; printf("%d\t", z);
    z = x * y; printf("%d\t", z);
    z = x / y; printf("%d\n", z);

    name[20] = "Fistum Mitiku"; sex[6] = "Male"; age = 33;
    printf("Hello %s! Your gender is %s and you are %d years old!\n", name, sex, age);

    int len = strlen(name); printf("The lengeth of your name is %d\n", len);
    int a = pow(6, 2); printf("The power of six is equal to %d\n", a);
    int b = 9; printf("The factorial of %d is equal to %d\n", b, f(b));

}