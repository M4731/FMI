#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>

int myFunct(char *fis, char *info, int m)
{
    FILE *f = fopen(fis,"r");
    if(f <= 0)
    {
        return -1;
    }

    char *g = malloc(sizeof(char) * m);
    fgets(g,m,f);
    fclose(f);

    f = fopen(fis,"w");
    if(f <= 0)
    {
        return -1;
    }

    fputs(g,f);
    fputs(info,f);
    fclose(f);
}

int main()
{
    myFunct("fin_fout1.txt","pere",8);
    return 0;
}