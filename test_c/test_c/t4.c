#include <stdio.h>

void person(char name[], char sex[], int age)
{
    printf("Hello %s! Your gender is %s and you are %d years old!\n", name, sex, age);
};
int main()
{
   
    person("Fistum", "Male", 32);
    person("Betty", "Female", 29);
    person("Mark", "Male", 34);
    
}
    
