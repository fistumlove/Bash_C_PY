#ifndef header_file
#define header_file

int x = 30;
int y = 20;
//int z;
 int z = 0;
//z = x + y; z = x - y; z = x * y; z = x / y;
int age;
char name[20] = "Fistum Mitiku";
char sex[6] = "Male";
char grade[5] = "A+";

int fact(int num)
{
    int count, fact = 1;
    for(count = 1; count <= num; count++)
    {
        fact = fact * count;
    }
    return fact;
}

#endif