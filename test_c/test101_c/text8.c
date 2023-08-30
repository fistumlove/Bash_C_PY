#include <stdio.h>
int main()
{
    const int maxInput = 5;
    double num, avg, sum = 0.0;
    int i;

    for(i = 1; i <= maxInput; i++)
    {
        printf("%d. Enter your number : ", i);
        scanf("%lf", &num);
        if(num < 0.0)
        {
            break;
        }
        sum += num;
    }
    avg = sum /(i - 1);
    printf("Sum = %.2lf\n", sum);
    printf("Avg = %.2lf\n", avg);
}