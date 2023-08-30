#include <stdio.h>
struct person 
{
    char name[10];
    char sex[6];
    int age;
};
int main()
{
    struct person p1 = {"Fistum", "Male", 23};
    struct person p2 = {"Betty", "Female", 28};
    struct person p3 = {"Kal", "Female", 32};

    printf("Hello %s! Your gender is %s and you're %d years old.\n", p1.name, p1.sex, p1.age);
    printf("Hello %s! Your gender is %s and you're %d years old.\n", p2.name, p2.sex, p2.age);
    printf("Hello %s! Your gender is %s and you're %d years old.\n", p3.name, p3.sex, p3.age);
}