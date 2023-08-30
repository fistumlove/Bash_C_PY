#ifndef header_file
#define header_file

int x = 39; int y = 86; int z; 
char name[20] = "Fistum Mitiku"; char sex[6] = "Male"; int age;

char car[10] = "TOYOTA!"; char model[10] = "COROLA";  char year[4] = "2023"; int i;

int f(int n)
{
    int i, f = 1;
    for(i = 1; i<=n; i++)
    {
        f = f*i;
    }
    return f;
}


#endif