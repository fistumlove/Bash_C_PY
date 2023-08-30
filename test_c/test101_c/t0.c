#include <stdio.h>
int addNum(int a, int b);
int main()
{
    int x, y, z;
    printf("Please enter your first number :\n");
    scanf("%d", &x);
    printf("Please enter your second number :\n");
    scanf("%d", &y);

    z = addNum(x, y);
    printf("Z = %d\n", z);

}
int addNum(int a, int b)
{
    int z;
    z = a + b;
    return z;
}