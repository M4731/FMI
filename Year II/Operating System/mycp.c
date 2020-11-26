#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>

const int MAX_BUFF_SIZE = 4096;

int main(int argc, char* argv[])
{
	int f = open(argv[1],O_RDONLY);
	if (f<0)
	{
		perror("nu s-a deschis fisierul de citire.");
		return errno;
	}
	else
	{
		printf("s-a deschis fisierul de citire.\n");
	}
	
	int h = open(argv[2], O_RDWR | O_CREAT | O_TRUNC, 0666);
	if (h<0)
	{
		perror("nu s-a deschis fisierul de scriere.");
		return errno;
	}
	else
	{
		printf("s-a deschis fisierul de scriere.\n");
	}
	
	struct stat sb;
	if(stat(argv[1],&sb))
	{
		perror("eroare");
		return errno;
	}
	printf("Fisierul de citire ocupa %jd bytes.\n",sb.st_size);
	
	char *buffer = malloc(MAX_BUFF_SIZE);
	int r = read(f,buffer,MAX_BUFF_SIZE);
	
	int variabilacarezicecatamdecitit = sb.st_size;
	while(r>0)
	{
		printf("S-au citit %d bytes.\n",r);
		if(variabilacarezicecatamdecitit>r)
			variabilacarezicecatamdecitit -= r;
		else
			variabilacarezicecatamdecitit=0;
		int w = write(h,buffer,r);
		if(w<0)
		{
			perror("eroare");
			return errno;
		}
		else
			printf("S-au scris %d bytes.\n",r);
		r = read(f,buffer,MAX_BUFF_SIZE);
	}

	free(buffer);
	close(f);
	close(h);
	return 0;	
}
