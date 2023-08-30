#include <stdio.h>
void desplay()
{
    desplay();
    desplay();
    desplay();
}
int main()
{
    

    static int x = 10;
    x += 5;

    printf("%d\n", x);
    printf("%d\n", x);
}