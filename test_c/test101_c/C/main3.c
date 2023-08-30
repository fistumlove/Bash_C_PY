#include <stdio.h>
void person(char name[10], char sex[6], int age)
{
    printf("Hello %s! Your gender is %s and you're %d years old.\n", name, sex, age);
};
int main()
{
    person("Fistum Mitiku", "Male", 24);
    person("Mike", "Male", 43);
    person("Kate", "Female", 24);
}