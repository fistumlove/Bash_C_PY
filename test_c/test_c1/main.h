#ifndef header_file
#define header_file

int x, y, z;
char name[20]; char sex[6]; int age;

int f(int n)
{
    int i, f =1;
    for(i = 1; i <= n; i++)
    {
        f = f*n;
    }
    return f;
}

#endif