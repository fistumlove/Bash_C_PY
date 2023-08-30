#include <stdio.h>
int main()
{
    int x[2][2][2];
    printf("Please enter your numbers below:\n");
    for(int i = 0; i < 2; i++)
    {
        for(int j = 0; j < 2; j++)
        {
            for(int k = 0; k < 2; k++)
            {
                printf("Please enter X%d%d%d : ", i+1, j+1, k+1);
                scanf("%d", &x[i][j][k]);
            }
        }
    }
    printf("Below are your lucky numbers:\n");
    for(int i = 0; i < 2; i++)
    {
        for(int j = 0; j < 2; j++)
        {
            for(int k = 0; k < 2; k++)
            {
                printf("Lucky Number X%d%d%d = %d \n", i+1, j+1, k+1, x[i][j][k]);
            }
        }
    }
}