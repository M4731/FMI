#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int count = 0;
void *increment()
{
    count++;
    return 0;
}

int main()
{
    pthread_t t[200];
    int i;

    for(i=0; i<200; i++)
    {
        pthread_create(&t[i], NULL, increment, NULL);
    }

    for(i=0; i<200; i++)
    {
        pthread_join(t[i], NULL);
    }

    printf("%d",count);
    printf("\n");
}