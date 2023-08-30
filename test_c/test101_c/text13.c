#include <stdio.h>
int main()
{
    int dayNum = 10;
    switch(dayNum)
    {
        case 0:
        printf("Sunday\n");
        break;
        case 1:
        printf("Monday\n");
        break;
        case 2:
        printf("Tuesday\n");
        break;
        case 3:
        printf("Wednsday\n");
        break;
        case 4:
        printf("Thursday\n");
        break;
        case 5:
        printf("Friday\n");
        break;
        case 6:
        printf("Saturday\n");
        break;
        default:
        printf("Invalid dayNum!\n");
        break;
    }
}