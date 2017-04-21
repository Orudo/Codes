#include"SeqList.h"
#include<iostream>
int main(){
	SeqList<int>* list=new SeqList<int>;
	cout<<"0"<<endl;
	for (int i=1;i<10;i++)
	{
		list->add(i);
	}
	cout<<"1"<<endl;
	list->listele();
	list->add(-1);
	list->listele();
	list->reverse();
	list->listele();
}
