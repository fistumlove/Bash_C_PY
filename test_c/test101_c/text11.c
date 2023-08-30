#include <stdio.h>
int main()
{
    int *x, y;
    y = 10;
    printf("The Value of Y = %d\n", y);
    printf("The location of Y = %p\n\n", &y);

    x = &y;
    printf("The Value of X = %d\n", *x);
    printf("The location of X = %p\n\n", x);

    *x = 15;
    printf("The Value of Y = %d\n", y);
    printf("The location of Y = %p\n\n", &y);

     printf("The Value of X = %d\n", *x);
    printf("The location of X = %p\n\n", x);
}