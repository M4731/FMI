#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include <stdio.h>
#include <sys/types.h>

int main()
{
	pid_t pid = fork();
	if (pid < 0)
	{
		perror("eroare");
		return errno;
	}
	else if (pid == 0)
	{
		char *argv[] = {"ls", NULL};
		printf("Child pid %d\n", getpid());
		execve ("/bin/ls", argv, NULL);
		perror("eroare");
	}
	else
	{
		printf("Parent pid %d\n", getpid());
		wait(NULL);
	}
}
