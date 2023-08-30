#include <stdio.h>
int main()
{
    int x[2][2], y[2][2], z[2][2];
    printf("Please enter your first matrix numbers below :\n");
    for(int i = 0; i < 2; i++)
    for(int j = 0; j < 2; j++)
    {
        printf("Enter X%d%d : ", i+1, j+1);
        scanf("%d", &x[i][j]);
    }
    printf("Please enter your second matrix numbers below :\n");
    for(int i = 0; i < 2; i++)
    for(int j = 0; j < 2; j++)
    {
        printf("Enter Y%d%d : ", i+1, j+1);
        scanf("%d", &y[i][j]);
    }
    printf("Desplay the sum of the matrix numbers below :\n");
    for(int i = 0; i < 2; i++)
    for(int j = 0; j < 2; j++)
    {
        z[i][j] = x[i][j] + y[i][j];
    }
    
    for(int i = 0; i < 2; i++)
    for(int j = 0; j < 2; j++)
    {
        printf("%d\t", z[i][j]);
        if(j == 1)
        printf("\n");
    }
}