#include <stdio.h>
const int city = 2;
const int days = 5;
int main()
{
    int temp[city][days];
    printf("Enter the temp of the week days for both cities:\n");
    for(int i = 0; i < city; i++)
    for(int j = 0; j < days; j++)
    {
        printf("Enter City%d : Day%d : ", i + 1, j + 1);
        scanf("%d", &temp[i][j]);
    }
    printf("Desplay the temp of the week days for both cities:\n");
    for(int i = 0; i < city; i++)
    for(int j = 0; j < days; j++)
    {
        printf("Desplay City %d : Day %d = %d\n", i + 1, j + 1, temp[i][j]);
        
    }
    
}