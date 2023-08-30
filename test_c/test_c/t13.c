#include <stdio.h>
int main()
{
    int num;
    printf("Please enter your day number : ");
    scanf("%d", &num);
    char DayNum;
    DayNum = num;
    switch(DayNum)
    {
        case 0:
        printf("Sunday!\n");
        break;
        case 1:
        printf("Monday!\n");
        break;
        case 2:
        printf("Tuesday!\n");
        break;
        case 3:
        printf("Wednesday!\n");
        break;
        case 4:
        printf("Thursday!\n");
        break;
        case 5:
        printf("Friday!\n");
        break;
        case 6:
        printf("Saturday!\n");
        break;
        default:
        printf("Invalied Day Num!\n");
        break;
    }
}