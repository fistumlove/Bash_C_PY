#include <stdio.h>
int main()
{
    char name[10];
    char sex[6];
    int age;

    printf("Please enter your name : ");
    scanf("%s", &name);
    printf("Please enter your sex : ");
    scanf("%s", &sex);
    printf("Please enter your age : ");
    scanf("%d", &age);

    printf("Hello %s! Your gender is %s and you're %d years old.", name, sex, age);
}