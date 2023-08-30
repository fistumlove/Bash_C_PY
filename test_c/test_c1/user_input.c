#include <stdio.h>
int main()
{
    char name[10];
    int id;
    char grade[1];
    printf("Please enter your name : ");
    scanf("%s", &name[10]);
    printf("Please enter your id : ");
    scanf("%d", &id);
    printf("Please enter your grade : ");
    scanf("%s", &grade[1]);

    printf("\nHello %s! Your student ID is %d and you got %s and successfully passed your exam!\n", name, id, grade);
    
}