#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		perror("nu sunt 2 argumente");
		return errno;
	}
	int s = atoi(argv[1]);
	pid_t pid = fork();
	if (pid < 0)
	{
		perror("eroare");
		return errno;
	}
	else if (pid == 0)
	{
		while(s != 1)
		{
			printf("%d ",s);
			if (s%2 == 0)
				s = s/2;
			else
				s = 3*s+1;
		}
	}
	else
	{
		printf("1. ");
		wait(NULL);
		printf("Child %d finished\n", pid);
	}
}
