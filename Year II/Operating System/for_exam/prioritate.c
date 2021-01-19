#include <stdio.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
struct stat st;

typedef struct
{
    char *nume;
    int prioritate;
} MYSTRUCT;

int myFunct(MYSTRUCT *p, int n)
{
    int s;

    MYSTRUCT *j = &p[0];
    for (int i = 1; i < n; i++)
    {
        if (j->prioritate < p[i].prioritate)
            j = &p[i];
    }

    int f = fork();
    if (!f)
    {
        return 0;
    }

    waitpid(f, s, 0);

    if (WIFEXITED(s))
    {
        if (WEXITSTATUS(s))
            return -1;
    }
    else
    {
        return -1;
    }

    return 0;
}

int main()
{
    for (int i = 0; i <= 10; i++)
    {
        if (fork())
            ;
        else
        {

            for (int j = 0; j < 200000; j++)
                ;
            return 0;
        }
    }

    return 0;
}