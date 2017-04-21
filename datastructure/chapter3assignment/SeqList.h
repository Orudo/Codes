#ifndef SEQLIST_H
#define SEQLIST_H
#include<cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
template<typename T>
class SeqList{
private:
	//de* minele=0;
	struct Node{
		/*friend bool operator < (Node* a,Node* b){
			return a->value<b->value;
		}*/
		T value;
		Node* next;
		//Node(T& val,Node* p):value(val),next(p){}
		T get_t(){return value;}
	};
	Node* minele=0;
	Node* head=0;
public:
	void add(T val){
		Node* node=new Node();
		node->value=val;
		node->next=head;
		head=node;
		if(!minele||head->value<minele->value)
		{
			minele=head;
		}
		clog<<"add succeed"<<endl;
	}
	T& getmin(){return minele->value;}
	void reverse(){
		Node* p=head->next;
		Node* pre=head;
		Node* next=p->next;
		head->next=0;
		while (next){
			p->next=pre;
			pre=p;
			p=next;
			next=p->next;
		}
		p->next=pre;
		head=p;
	}
	void listele(){
		clog<<"list"<<endl;
		Node* p=head;
		while (p){
				cout<<p->value;
				p=p->next;
		}
		std::cout<<std::endl;
	}
};


#endif
