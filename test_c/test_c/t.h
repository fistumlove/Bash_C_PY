#ifndef header_file
#define header_file

int x = 34;
int y = 69;
int z;
char name[20] = "Fistum Mitiku";
char sex[6] = "Male";
int age = 29;

int f(int n)
{
    int i, f = 1;
    for(i=1; i<=n; i++)
    {
        f = f * i;
    }
    return f;
}
#endif