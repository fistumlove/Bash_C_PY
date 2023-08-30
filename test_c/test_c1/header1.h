#ifndef header_file
#define header_file

int x, y, z;
char name[20] = "Fistum Girum"; char citizen[15] = "USA"; char city[15] = "Seattle";

int f(int n)
{
    int i, f = 1;
    for(i = 1; i <= n; i++)
    {
        f = f * i;
    } 
    return f;

}

#endif