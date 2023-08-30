#include <stdio.h>
int addNum(int a, int b);
int main()
{
    int x, y, z = 0;
    printf("Please enter your first number : ");
    scanf("%d", &x);
    printf("Please enter your second number : ");
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