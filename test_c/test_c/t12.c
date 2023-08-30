#include <stdio.h>
int main()
{
    const int maxIn = 5;
    double num, sum, avg = 0.0;
    int i;

    for(i = 1; i <= maxIn; i++)
    {
        printf("%d. Please enter your numbers :", i);
        scanf("%lf", &num);
        sum += num;
        avg = sum / i;
    }
    printf("Sum = %.2lf\n", sum);
    printf("Avg = %.2lf\n", avg);
}