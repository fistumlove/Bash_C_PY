#include <stdio.h>

// For loop

int main()
{
    int i;
    char name[] = "Fistum G Mitiku";
    for(i = 0; i <= 15; i++)
    {
        printf("%c\t", name[i]);
        printf("%d\n", i);
    }
}

//While
/*
int main()
{
    int i;
    char name[] = "Welcome to my world!";
    while(i < 20)
    {
        printf("%c\n", name[i]);
        i++;
    }
}

*/

//Do
/*
int main()
{
    int i;
    char name[] = "Welcome to my world!";
    do
    {
        printf("%c\n", name[i]);
        i++;
    }
    while(i < 20);
}

*/


