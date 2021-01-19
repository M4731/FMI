#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
    int i;
    char * arg[] = {"./progB","a","b",NULL};
    for(i=0; i<argc; i++)
    {
        printf("%s", argv[i]);
    }
    execve("./progB",arg, NULL);
    return 0;
}