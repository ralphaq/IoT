#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
//#include <stdbool>

struct Node{
	int data;
	struct Node* next;
};

void printlist( struct Node* n){
	while(n!=NULL){
		printf("%d",n->data);
		n=n->next;
	}
}

int getcount(struct Node* head){
	int count=0;
	struct Node* current=head;
	while(current!=NULL){
		count++;
		current=current->next;
	}
	return count;
}
int search(struct Node* head,int value){
	struct Node* current=head;
	while(current!=NULL){
		if(current->data==value)
			return 1;
		current=current->next;
	}
	return 0;
}

int smallestElement(struct Node* head){
	int min=INT_MAX;
	while(head!=NULL){
		if(min>head->data)
			min=head->data;
		head=head->next;
	
	}
	return min;


}
int maximumElement(struct Node* head){
	int max=INT_MIN;
	while(head!=NULL){
		if(max<head->data)
			max=head->data;
		head=head->next;
	}
	return max;
}

int print2largest(struct Node* head){
	int i,first,second;
	int list_size=getcount(head);
	if(list_size<2){
		printf("invalid input\n");
		return 0;
	}
	first=second=INT_MIN;
	struct Node* temp=head;
	while(temp!=NULL){
		if(temp->data>first){
			second=first;
			first=temp->data;
		}
		else if(temp->data >second && temp->data!=first)
			second=temp->data;
		temp=temp->next;
	}
	//if(second=INT_MIN)
	//	printf("there is no second element\n");
	//else
		//printf("the second largest element is : %d\n",second);
	return second;
}
int main(){
	struct Node* head =NULL;
	struct Node* second =NULL;
	struct Node* third =NULL;

	//allocate three nodes in heap
	
	head=(struct Node*)malloc(sizeof(struct Node));
	second=(struct Node*)malloc(sizeof(struct Node));
	//third = (struct Node*)malloc( sizeof(struct  Node));
	third = (struct Node*)malloc(sizeof(struct Node));

	head->data=1;
	head->next=second;

	second->data=2;
	second->next=third;

	third->data=3;
	third->next=NULL;

	printlist(head);
	printf("\n");
	printf("No. of node in linklist is : %d\n",getcount(head));
	search(head, 2)? printf("Yes\n") : printf("No");
	printf("maximum element : %d\n",maximumElement(head));
	printf("minimum element : %d \n",smallestElement(head));
	printf("second largest element is: %d\n",print2largest(head));	
			



	return 0;

}

