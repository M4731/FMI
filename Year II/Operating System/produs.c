#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>       
#include <string.h> 
#include <errno.h>
//se ruleaza cu -pthread la final :D
#include <pthread.h>
int **mat1, **mat2;

struct ooooo
{
	int x, y, z;
};

void* func(void* ceva)
{
	struct ooooo *xyz=ceva;
	int *sum=(int *)malloc(sizeof(int));
	*sum = 0;
	for(int i=0; i<xyz->z; i++)
	{
		*sum += mat1[xyz->x][i] * mat2[i][xyz->y];
	}
	return sum;
}

int main()
{
	int m1, n1, m2, n2;
	printf("Dimensiuni prima matrice: ");
	scanf("%d %d",&m1, &n1);
	
	mat1 = (int**)malloc(sizeof(int*)*m1);
	printf("Elemente prima matrice: ");
	for(int i=0; i<m1; i++)
	{
		mat1[i] = (int*)malloc(sizeof(int)*n1);
		for(int j=0; j<n1; j++)
		{
			int x;
			scanf("%d",&x);
			mat1[i][j] = x;
		}
	}
	
	printf("Dimensiuni a doua matrice: ");
	scanf("%d %d",&m2, &n2);
	
	mat2 = (int**)malloc(sizeof(int*)*m2);
	printf("Elemente prima matrice: ");
	for(int i=0; i<m2; i++)
	{
		mat2[i] = (int*)malloc(sizeof(int)*n2);
		for(int j=0; j<n2; j++)
		{
			int x;
			scanf("%d",&x);
			mat2[i][j] = x;
		}
	}
	
	pthread_t thr[m1*n2];
	int r[m1][n2];
	int q = 0;
	
	for(int i=0; i<m1; i++)
	{	
		for(int j=0; j<n2; j++)
		{
			struct ooooo *xyz=(struct 					ooooo*)malloc(sizeof(struct ooooo));
			xyz->x = i;
			xyz->y = j;
			xyz -> z = m2;
			
			if(pthread_create(&thr[q++], NULL, func, xyz))
			{
				perror("Nu s-a creat corect threadul.");
				return errno;
			}
		}
	}
	
	q = 0;
	void *res;
	for(int i=0; i<m1; i++)
	{	
		for(int j=0; j<n2; j++)
		{
			if(pthread_join(thr[q++], &res))
			{
				perror("Nu s-a reusit asteptarea");
				return errno;
			}
			r[i][j] = *((int*) res);
		}
	}
	
	for(int i=0; i<m1; i++)
	{	
		for(int j=0; j<n2; j++)
		{
			printf("%d ",r[i][j]);
		}
		printf("\n");
	}	
}
