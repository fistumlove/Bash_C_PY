#include <stdio.h>
int addNum(int a, int b);
int main()
{
    int x, y, z;

    printf("Please enter your first number : ");
    scanf("%d", &x);
    printf("Please enter your second number : ");
    scanf("%d", &y);
    z = addNum(x, y);
}
int addNum(int a, int b)
{
    int z;
    z = a + b;
    return z;
}