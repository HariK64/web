#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#define SIZE 1024
void main(){
	int pfd[2];
	int nread;
	int pid;
	char buf[SIZE];
	pipe(pfd);
	if((pid = fork())<0){
		perror("Fork failed");
		exit(2);
	}
	else if(pid==0){
		close(pfd[0]);
		printf("Enter string");
		scanf("%s", buf);
		write(pfd[1], buf, strlen(buf)+1);
		close(pfd[1]);
	}
	else{
		close(pfd[1]);
		char *s;
		read(pfd[0], buf, SIZE);
		for(int i=0;i<strlen(buf);i++){
			if(!isupper(buf[i]))
				buf[i] = buf[i] - 32;
			
		}
		printf("%s\n", buf);
		close(pfd[0]);
	}
}