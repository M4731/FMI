#include <stdio.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>
struct stat st;

int myFunct(char **fin, int nr, char *fout)
{
    FILE *g = fopen(fout, "w+");
    if (g <= 0)
    {
        return -1;
    }

    for (int i = 0; i < nr; i++)
    {

        FILE *f = fopen(fin[i], "r");

        if (f <= 0)
        {
            return -1;
        }
        stat(fin[i], &st);
        int n = st.st_size;
        n++;
        char *s = malloc(sizeof(char) * n);
        fgets(s, n, f);
        fputs(s, g);

        fclose(f);
        free(s);
    }

    fclose(g);
    return 0;
}

int main()
{
    char **f;
    f = malloc(2 * sizeof(char *));
    f[0] = malloc(256);
    f[1] = malloc(256);

    strcpy(f[0], "fin_fout1.txt");
    strcpy(f[1], "fin_fout2.txt");
    printf("%s\n", f[0]);
    return myFunct((char **)f, 2, "fin_fout3.txt");
}