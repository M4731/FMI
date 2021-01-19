#include <unistd.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

void myFunct(char *fis, int *val)
{
    FILE *f = fopen(fis, "rb");

    int min = INT_MAX;
    int i = 0;

    if (!f)
    {
        *val = -1;
        return;
    }
    for (int j = 0; fread(&i, sizeof(int), 1, f); j++)
    {

        //printf("%i\n", i);
        if (min > i)
        {
            *val = j;
            min = i;
        }
    }
    if (!feof(f))
    {
        *val = -1;
    }
}

int main()
{
    FILE *f = fopen("minim_binar.bin", "wb");

    for(int i = 100; i>=0; i--)
    {
        fwrite(&i, sizeof(int), 1, f);
    }
    fclose(f);

    int *o;

    myFunct("minim_binar.bin",o);
    printf("%d\n",*o);

}