#include <stdio.h>
void checkPN();
int main()
{
    checkPN();
}
void checkPN()
{
    int n, i, flag = 0;
    printf("Please enter your number : ");
    scanf("%d", &n);
    if(n == 0 || n == 1)
    flag = 1;
    for(i = 2; i <= n/2; i++)
    {
        if(n%i == 0)
        {
            flag = 1;
            break;
        }
        printf("\ni=%d\n",i);
    }
    if(flag == 1)
    printf("%d is not a prime number!\n", n);
    else
    printf("%d is a prime number!\n", n);
}