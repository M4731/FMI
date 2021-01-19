// Scrieti o functie int myFunct(char *fis) care deschide fisierul BINAR cu numele fis si dintre numerele intregi din el le va sterge pe cele de valoare maxima. 
// Functia intoarce -1 in caz de eroare, alfel 0. 
// P.S.: Este permisa folosirea unui fisier auxiliar (care sa nu existe deja in director si care sa fie sters inainte de return), 
// dar nu este permisa maparea fisierului in memorie.

#include <unistd.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int myFunct(char *fis)
{
    FILE *f = fopen(fis,"rb");
    if(f <= 0 )
    {
        return -1;
    }
    
    int a=0, maxim = INT_MIN;
    
    for(int i = 1; fread(&a, sizeof(int), 1, f); i++)
    {
        if(maxim < a)
        {
            maxim = a;
        }
    }

    if(!feof(f))
    {
        return -1;
    }
    fclose(f);


    FILE *aux = fopen("aux.bin","wb");
    f = fopen(fis,"rb");
    if(f <= 0 )
    {
        return -1;
    }
    
    for(int i = 1; fread(&a, sizeof(int), 1, f); i++)
    {
        if(maxim != a)
        {
            fwrite(&a, sizeof(int), 1, aux);
        }
    }

    if(!feof(f))
    {
        return -1;
    }
    fclose(f);
    fclose(aux);

    remove("stergere_maxim.bin");
    rename("aux.bin", "stergere_maxim.bin");

    return maxim;
}

int main()
{
    // FILE *f = fopen("stergere_maxim.bin", "wb");

    // int i = malloc(sizeof(int));
    // for(int i = 1; i<=100; i++)
    // {
    //     fwrite(&i, sizeof(int), 1, f);
    // }
    // fclose(f);

    int o = myFunct("stergere_maxim.bin");
    printf("%d\n",o);
}