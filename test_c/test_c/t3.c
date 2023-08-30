#include <stdio.h>

int main()
{
    char name[5];
    char sex[4];
    int age;

    printf("Please enter your name : \n");
    scanf("%s", &name[5]);
    printf("Please enter your gender : \n");
    scanf("%s", &sex[4]);
    printf("Please enter your age : \n");
    scanf("%d", &age);

    printf("Hello %s! Your gender is %s and you are %d years old!\n", name, sex, age);

}