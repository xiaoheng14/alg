#include<stdio.h>
#include<malloc.h>

#define DataType int
#define MAXSIZE 1024

# 栈的顺序表简单实现

struct SeqStack {
	DataType data[MAXSIZE];
	int top;
};

SeqStack* initSeqStack(){
	SeqStack* s = (SeqStack*)malloc(sizeof(SeqStack));
	if(!s){
		printf("no free room");
		return NULL;
	}
	s -> top = -1;
	return s;
}

bool isEmptySeqStack(SeqStack* s) {
	if(s->top == -1)
		return true;
	return false;
}

int pushSeqStack(SeqStack* s, DataType x) {
	if(s->top == MAXSIZE -1) {
		printf("栈满");
		return -1;
	} else {
		s->top ++;
		s->data[s->top] = x;
		return 0;
	}
}

int popSeqStack(SeqStack* s, DataType* x) {
	if(isEmptySeqStack(s)) {
		printf("栈空");
		return -1;
	} else {
		*x = s->data[s->top];
		s->top--;
		return 0;
	}
}

int topSeqStack(SeqStack* s, DataType* x) {
	if(isEmptySeqStack(s)) {
		return -1;
	} else {
		*x = s->data[s->top];
		return 0;
	}
}

int printSeqStack(SeqStack* s){
	int i;
	for(i = s->top; i>=0; i--){
		printf("%4d", s->data[i]);
	}
	return 0;
}

int main(){
	SeqStack* seq = initSeqStack();
	if(!seq) {
		return -1;
	}
	pushSeqStack(seq, 4);
	pushSeqStack(seq, 6);
	printSeqStack(seq);
	
	DataType x = 0;
	int ret = topSeqStack(seq, &x);
	printf("top is %d\n", x);
	ret = popSeqStack(seq, &x);
	printf("\n");
	printSeqStack(seq);
	return 0;
}
