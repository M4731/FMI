#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/errno.h>
#include <sys/mman.h>
#include <sys/stat.h>        
#include <fcntl.h> 

int main(int argc, char * argv[])
{
	char* shm_name = "myshm";
	int shm_fd;
	
	printf("Starting parent %d\n", getpid());
	
	if (argc == 1)
	{
		perror("nu sunt cle putin 2 argumente.\n");
		return errno;
	}
	
	shm_fd = shm_open(shm_name, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
	if (shm_fd < 0)
	{
		perror("nu s-a putut crea memoria partajata.\n");
		return errno;
	}
	
	size_t shm_size = argc * getpagesize();
	
	if(ftruncate(shm_fd, shm_size) == -1)
	{
		perror("nu s-a putut trunchia memoria partajata.\n");
		shm_unlink(shm_name);
		return errno;
	}	
	
	for (int i=1; i<argc; i++)
	{
		int s = atoi(argv[i]);
		pid_t pid = fork();
		
		if (pid < 0)
		{
			perror("eroare\n");
			return errno;
		}
		else if (pid == 0)
		{
			int *shm_ptr;
			int k = 0;
			shm_ptr = mmap(0, getpagesize(), PROT_WRITE, 					MAP_SHARED, shm_fd, getpagesize()*(i-1) );
			
			if(shm_ptr == MAP_FAILED)
			{
			 	perror("maparea a esuat.");
			 	shm_unlink(shm_name);
			 	return errno;
			}
			
			while(s != 1)
			{
				shm_ptr[k] = s;
				k+=1;
				 
				if (s%2 == 0)
					s = s/2;
				else
					s = 3*s+1;
			}
		shm_ptr[k] = 1;
		printf("Done Parent %d Me %d\n",getppid(),getpid());
		
		munmap(shm_ptr,getpagesize());
		
		return 0;
		}
	}
	
	for (int i=1; i<argc; i++)
	{
		wait(NULL);
		
		int *shm_ptr;
		int k = 0;
		shm_ptr = mmap(0, getpagesize(), PROT_READ, 					MAP_SHARED, shm_fd, getpagesize()*(i-1) );
		
		if(shm_ptr == MAP_FAILED)
		{
		 	perror("maparea a esuat.\n");
		 	shm_unlink(shm_name);
		 	return errno;
		}
		
		printf("%d : ",shm_ptr[k]);
		while(shm_ptr[k] != 1)
		{
			printf("%d ",shm_ptr[k]);
			k+=1;
		}
		printf("%d.\n",shm_ptr[k]);
		
		munmap(shm_ptr,getpagesize());
		
	}
	printf("Done Parent %d Child %d finished\n", getppid(),getpid());
	
	shm_unlink(shm_name);
}
