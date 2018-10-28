#include <stdio.h> 
#include <sys/ipc.h> 
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
void main(){
	int shmid;
	char *a, *b;

	shmid=shmget(IPC_PRIVATE, 5*sizeof(char), 0777|IPC_CREAT);
	pid_t pid = fork();
	if(pid<0){
	exit(0);
	}
	else if(pid==0){
		b = shmat(shmid, 0,0);
		printf("Enter a string");
		char* s;
		scanf("%s", s);
		for(int i=0;s[i]!=NULL;i++){
			if(!isupper(s[i]))
				s[i] = s[i] - 32;
			b[i] = s[i];
		}
		shmdt(b);
	}
	else{
		wait();
		a = shmat(shmid,0,0);
		printf("%s\n", a);
		shmdt(a);
		shmctl(shmid, IPC_RMID, 0); 
	}
}