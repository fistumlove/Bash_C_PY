#include "header.h"
#include <stdio.h>

void person(char name[10], char sex[1], int age)
{
    printf("Hello %s! Your gender is %s and you are %d years old!\n", name, sex, age);
}
int main()
{
    person("Fistum", "M", 32);
    person("Mike", "M", 39);
    person("Betty", "F", 28);
}