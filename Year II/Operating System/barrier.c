#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>       
#include <string.h> 
#include <errno.h>
//se ruleaza cu -pthread la final :D
#include <pthread.h>
#include <semaphore.h>

pthread_mutex_t mtx;
sem_t sem;
int S=0;
int nr_repetari = 5;

void barrier_point()
{
	pthread_mutex_lock(&mtx);
	S+=1;
	if(S==nr_repetari)
	{
	 	pthread_mutex_unlock(&mtx);
	 	for(int i=0; i<nr_repetari; i++)
	 	{
	 		sem_post(&sem);
	 	}
	 	
	}
	else
	{
		pthread_mutex_unlock(&mtx);
		sem_wait(&sem);
	}
}

void *tfun(int x)
{
	printf("%d reached the barrier\n",x);
	barrier_point();
	printf("%d passed the barrier\n",x);
	
	return NULL;
}

int main()
{
	if(pthread_mutex_init(&mtx, NULL))
	{
		perror("Nu s-a putut initializa mutexul.");
		return errno;
	}
	
	if(sem_init(&sem, 0, S))
	{
		perror("Nu s-a putut initializa semaforul.");
		return errno;
	}
	
	pthread_t thr[nr_repetari];
	for(int i=0; i<nr_repetari; i++)
	{
		if(pthread_create(&thr[i], NULL, tfun, i))
		{
			perror("Nu s-a creat corect threadul.");
			return errno;
		}
	}
	
	
	for(int i=0; i<nr_repetari; i++)
	{
		if(pthread_join(thr[i], NULL))
		{
			perror("Nu s-a reusit asteptarea");
			return errno;
		}

	}	
		
	pthread_mutex_destroy(&mtx);	
}
