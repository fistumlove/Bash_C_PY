#include <stdio.h>
int addNum(int a, int b);
int main()
{
    int x, y, z;
    printf("Please enter your number : ");
    scanf("%d", &x);
    printf("Please enter your number : ");
    scanf("%d", &y);
    z = addNum(x, y);
    printf("Sum = %d\n", z);   
}
int addNum(int a, int b)
{
    int sum;
    sum = a + b;
    return sum;
}