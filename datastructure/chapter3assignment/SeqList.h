#ifndef SEQLIST_H
#define SEQLIST_H
#include<cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
template<typename T>
class SeqList{
private:
	struct Node{
		T value;
		Node* next;
		T get_t(){return value;}
		bool isDel=false;
	};
	Node* Tree[10000]={0};
	int T_acc[10000];
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
		add_t(node,1);
	}
	int getPredessor(int pos)
	{
		if(Tree[pos*2])
			return get_rightleaf(pos*2);
		else return 0;
	}
	int get_rightleaf(int pos)
	{
		if(!Tree[pos*2+1])
		return pos;
		else return get_rightleaf(pos*2+1);
	}
	int getSuccessor(int pos)
	{
		if (Tree[pos*2+1])
			return get_leftleaf(pos*2+1);
		else return 0;
	}
	int get_leftleaf(int pos)
	{
		if(!Tree[pos*2])
			return pos;
		else return get_leftleaf(pos*2);
	}
	int getNode(T val,int pos)
	{
		if(!Tree[pos]) return 0;
		if(Tree[pos]->value==val)
		{
			return pos;
		}
		return getNode(val,pos*2)|getNode(val,pos*2+1);

	}
	void add_t(Node* p,int pos)
	{	
		if(!Tree[pos])
		{
			clog<<"add to"<<pos<<endl;
			Tree[pos]=p;
			T_acc[pos]=1;
		}
		if(p->value<Tree[pos]->value)
			add_t(p,pos*2);
		if(p->value==Tree[pos]->value)
			T_acc[pos]++;
		if(p->value>Tree[pos]->value)
			add_t(p,pos*2+1);
	}
	T* getmin(){return getmin_rec(1);}
	T* getmin_rec(int pos)
	{
		if(!Tree[pos*2])
			return Tree[pos];
		else return getmin_rec(pos*2);
	}
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
	void reverse_rec()
	{
		rec(head)->next=0;
	}
	Node* rec(Node* p)
	{
		if(!p->next)
		{
			head=p;
			return p;
		}
		rec(p->next)->next=p;
		return p;
	}
	void print_sorted(int pos)
	{
		if(Tree[pos])
		{
			print_sorted(pos*2);
			cout<<Tree[pos]->value<<' ';
			print_sorted(pos*2+1);
		}
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
