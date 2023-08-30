#include <stdio.h>
void checkPN();
int main()
{
    checkPN();
}
void checkPN()
{
    int i, n, flag;

    printf("Enter a prime number : ");
    scanf("%d", &n);
    for(i = 2; i <= n/2; i++)
    {
        if(n == 0 || n == 1)
        flag = 1;
        if(n%i < 1)
        {
            flag = 1;
            break;
        }
    }
    if(flag == 1)
    printf("%d is not a prime number!", n);
    else
    printf("%d is a prime number!", n);
}