#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>       
#include <string.h> 
#include <errno.h>
//se ruleaza cu -pthread la final :D
#include <pthread.h>

void* func(void* s)
{
	char* x = (char *)s;
	char* rez = malloc(strlen(x) * sizeof(char));
	int k =0;
	for(int i=strlen(x)-1; i>=0; i--)
	{
		rez[k] = x[i];
		k++;
	}
	return rez;
}

int main(int argc, char* argv[])
{
	char* s = argv[1];
	printf("Cuvant initial: %s\n", s);
	
	pthread_t thr;
	if(pthread_create(&thr, NULL, func, s))
	{
		perror("Nu s-a creat corect threadul.");
		return errno;
	}
	
	char* result;
	
	if(pthread_join(thr, &result))
	{
		perror("Nu s-a reusit asteptarea");
		return errno;
	}
	
	printf("Cuvant rasturnat: %s\n", result);
	free(result);
}


