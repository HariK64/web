#include <stdio.h> 
#include <sys/ipc.h> 
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
void main(){
	int shmid, status;
	int *a, *b;

	shmid=shmget(IPC_PRIVATE, 1*sizeof(int), 0777|IPC_CREAT);
	pid_t pid = fork();
	if(pid<0){
	exit(0);
	}
	else if(pid==0){
		b = (int*)shmat(shmid, 0,0);
		for(int i=0;i<10;i++){
			int n;
			printf("Enter no");
			scanf("%d", &n);
			b[0]=n;
			sleep(1);
		}
		wait(&status);
		shmdt(b);
	}
	else{
		
		a = (int*)shmat(shmid,0,0);
		for(int i=0;i<10;i++){
			sleep(1);
			printf("parent %d", a[0]);
		}
		shmdt(a);
		shmctl(shmid, IPC_RMID, 0); 
	}
}