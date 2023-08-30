#include <stdio.h>  
#include <string.h>  
#include <math.h>  
int main()  
{  
  char s1[20] = "TechVidvan";  
  char s2[15] = "Tutorial";  
  printf("TechVidvan Tutorial: Example of header files in C!\n\n");
  int num = pow(4, 3); // pow() function from math.h header file!
  printf("Value of num: %d\n", num);  
  int len = strlen(s1); // strlen() function from string.h header file!
  printf("String s1’s length is: %d", len);  
  return 0;  
}