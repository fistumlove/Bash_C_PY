#include <stdio.h>

int main()
{
    char name[] = "Mark";
    int i;

    do
    {
        printf("%c\t", name[i]);
        i++;
    } 
    while (i < 5);
    
}

/*
int main()
{
    char name[6] = "FISTUM";
    int i;

    while(i < 6)
    {
        printf("\n%c\t", name[i]);
        i++;
    }
}

int main()
{
    char name[6] = "Fistum";

    for(int i =0; i < 8; i++)
    {
        printf("%c\n", name[i]);
    }
}
*/
