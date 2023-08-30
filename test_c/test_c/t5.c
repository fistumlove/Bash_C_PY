#include <stdio.h>

struct person
{
    char name[10];
    char sex[6]; 
    int age;
};
int main()
{
    struct person p1 = {"Fistum", "Male", 33};
    struct person p2 = {"Merry", "Female", 31};
    struct person p3 = {"Mark", "Male", 23};

    printf("Hello %s! You are %s and your age is %d.\n", p1.name, p1.sex, p1.age);
    printf("Hello %s! You are %s and your age is %d.\n", p2.name, p2.sex, p2.age);
    printf("Hello %s! You are %s and your age is %d.\n", p3.name, p3.sex, p3.age);

}