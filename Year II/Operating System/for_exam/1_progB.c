#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
    int i;
    for(i=0; i<argc; i++)
    {
        printf("%s", argv[i]);
    }
    return 0;
}