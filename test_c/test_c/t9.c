#include <stdio.h>
const int citys = 2;
const int days = 4;
int main()
{
    int temp[citys][days];
    printf("Please enter your temp of the week for city 1:\n");
    for(int i = 0; i < citys; i++ )
    for(int j = 0; j < days; j++)
    {
        printf("Enter City%d : Days%d : ", i+1, j+1);
        scanf("%d", &temp[i][j]);
    }
   
    printf("Desplay the temp of the week for both cities:\n");
    for(int i = 0; i < citys; i++ )
    for(int j = 0; j < days; j++)
    {
        printf("Temp of City%d : Days%d = %d\n", i+1, j+1, temp[i][j]);
    }
}