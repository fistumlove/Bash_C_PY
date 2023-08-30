#include "header.h"
#include <stdio.h>

int main()
{
    printf("Please enter your name : ");
    scanf("%s", &name[10]);
    printf("Please enter your gender : ");
    scanf("%s", &sex[1]);
    printf("Please enter your age : ");
    scanf("%d", &age);

    printf("Hello %s! Your gender is %s and you are %d years old!\n", name, sex, age);
}