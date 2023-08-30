#include <stdio.h>

void person(char name[], int id, char grade[])
{  
    printf("Hello %s! Your ID is %d and you got %s passed your exam!\n", name, id, grade);
};
int main()
{
    person("Fistum", 101, "A");
    person("Mike", 201, "B");
    person("Betty", 301, "C");
}


// struct

/*
struct person
{
    char name[10];
    int id; 
    char grade[1];
};
int main()
{
    struct person p1 = {"Fistum", 101, "A"};
    struct person p2 = {"Mike", 201, "B"};
    struct person p3 = {"Betty", 301, "C"};
    printf("Hello %s! Your ID is %d and you got %s passed your exam!\n", p1.name,p1.id,p1.grade);
    printf("Hello %s! Your ID is %d and you got %s passed your exam!\n", p2.name,p2.id,p2.grade);
    printf("Hello %s! Your ID is %d and you got %s passed your exam!\n", p3.name,p3.id,p3.grade);
}
*/