//Scrieti o functie int myFunct(char *fis, int m, int *n) care deschide fisierul BINAR cu numele fis si citeste de la pozitia m din fisier *n valori intregi.
//Functia va calcula minimul dintre aceste valori si il va returna. 
//In caz de eroare, in pointerul n se va stoca valoarea -1, altfel 0.
#include <unistd.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int myFunct(char *fis, int m, int *n)
{
    FILE *f = fopen(fis,"rb");
    if(f <= 0 )
    {
        *n = -1;
        return -1;
    }
    
    int a=0, minim = INT_MAX, q = *n;
    //printf("%d\n",q);
    for(int i = 1; fread(&a, sizeof(int), 1, f); i++)
    {
        //printf("%d\n",i);
        //printf("%d\n",a);
        if(i >= m && q > 0)
        {
            if(minim > a)
            {
                minim = a;
            }
            q--;
        }
    }

    if(feof(f))
    {
        fclose(f);
        return minim;
        *n = 0;
    }
    *n = -1;
    return -1;
}

int main()
{
    FILE *f = fopen("minim_binar.bin", "wb");

    //int i = malloc(sizeof(int));
    for(int i = 99; i>0; i--)
    {
        fwrite(&i, sizeof(int), 1, f);
    }
    fclose(f);

    int nr = 20;
    int o = myFunct("minim_binar.bin",20, &nr);
    printf("%d\n",o);
}