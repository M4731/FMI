#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>       
#include <string.h> 
#include <errno.h>
//se ruleaza cu -pthread la final :D
#include <pthread.h>

#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
pthread_mutex_t mtx;

int decrease_count(int count)
{
	if(available_resources < count)
		return -1;
	else 
		available_resources -= count;
	return 0;
}

int increase_count(int count)
{
	available_resources += count;
	return 0;
}

void func(void* count)
{
	int x = (int)count;
	pthread_mutex_lock(&mtx);
	
	if(decrease_count(x) == -1)
	{
		printf("Eroare: nu am destule resurse\n");
		pthread_mutex_unlock(&mtx);
	}
	else
	{
		printf("Got %d resources %d remaining\n", x, 			    available_resources);
		pthread_mutex_unlock(&mtx);
		
		increase_count(x);
		printf("Released %d resources %d remaining\n", x, 		    available_resources);
	}
}


int main()
{
	printf("MAX_RESOURCES=%d\n",available_resources);
	
	if(pthread_mutex_init(&mtx, NULL))
	{
		perror("Nu s-a putut initializa mutexul.");
		return errno;
	}
	
	int nr_repetari = 5;
	pthread_t thr[nr_repetari];
	for(int i=0; i<nr_repetari; i++)
	{
		int x = rand()%MAX_RESOURCES;
		
		if(pthread_create(&thr[i], NULL, func, x))
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
