#include <stdlib.h>
#include <stdio.h>
int main(){
int *point;
point = malloc(10 * sizeof(*point)); // block of 15 integers!
*(point + 1) = 10; /* assign 480 to sixth integer */
printf("Value of second integer is %d",*(point + 1));
}