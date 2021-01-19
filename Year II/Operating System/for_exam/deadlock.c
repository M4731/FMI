#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

pthread_mutex_t mtxA, mtxB;
int accA=10, accB=10;

void *A_trans_B()
{
    pthread_mutex_lock(&mtxA);
    sleep(2);
    printf("a\n");
    accA--;
    pthread_mutex_lock(&mtxB);

    printf("b2\n");
    accB++;

    pthread_mutex_unlock(&mtxA);
    pthread_mutex_unlock(&mtxB);

    return 0;
}

void *B_trans_A()
{
    pthread_mutex_lock(&mtxB);
    sleep(2);

    printf("b\n");

    accB--;
    pthread_mutex_lock(&mtxA);

    printf("a2");

    accA++;
    pthread_mutex_unlock(&mtxB);
    pthread_mutex_unlock(&mtxA);

    return 0;
}

int main()
{
    pthread_t t1, t2;
    pthread_mutex_init(&mtxA, NULL);
    pthread_mutex_init(&mtxB, NULL);

    pthread_create(&t1, NULL, *A_trans_B, NULL);
    pthread_create(&t2, NULL, *B_trans_A, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_mutex_destroy(&mtxA);
    pthread_mutex_destroy(&mtxB);
}