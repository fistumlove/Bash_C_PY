#include <stdio.h>
void checkPN();
int main()
{
    checkPN();
}
void checkPN()
{
    int i, num, flag;
    printf("Please enter your number : \n");
    scanf("%d", &num);
    for(int i = 2; i <= num/2; i++)
    {
        if(num%i < 1)
        {
            flag = 1;
            break;
        }

        if(num == 0 || num == 1)
        flag = 1;
         
    }
    if(flag == 1)
    printf("%d is not a prime number!\n", num);
    else
    printf("%d is a prime number!\n", num);
}