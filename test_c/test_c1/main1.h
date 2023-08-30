#ifndef header_file
#define header_file

int x, y, z;
char name[20] = "Fistum Mitiku"; char sex[6] = "male"; int age = 27;

int f(int n)
{
    int i, f =1;
    for(i = 1; i <= n; i++)
    {
        f = f* i;
    }
    return f;
}

#endif