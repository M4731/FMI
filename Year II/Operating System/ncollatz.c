#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	if (argc == 1)
	{
		perror("nu sunt cle putin 2 argumente");
		return errno;
	}
	for (int i=1; i<argc; i++)
	{
		int s = atoi(argv[i]);
		pid_t pid = fork();
		
		if (pid < 0)
		{
			perror("eroare");
			return errno;
		}
		else if (pid == 0)
		{
			printf("%d: ",s);
			while(s != 1)
			{
				printf("%d ",s);
				if (s%2 == 0)
					s = s/2;
				else
					s = 3*s+1;
			}
			printf("1. \n");
			printf("Done Parent %d Me %d\n",getppid(),getpid());
			return 0;
		}
	}
	for (int j=1; j<argc; j++)
	{
		wait(NULL);
	}
	printf("Done Parent %d Child %d finished\n", getppid(),getpid());
}
