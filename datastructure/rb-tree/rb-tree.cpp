#include<cstdio>
#include<cstlib>


using namespace std;


struct Node{
	int data;
	int color;
	Node* p,ls,rs;
	Node* linkto(int to,int dir){this->p=to;to->s[dir]=this;return to;}
	int getlr(){return this==this->p->s[1];}
}


int main(){
	return 0;
}
