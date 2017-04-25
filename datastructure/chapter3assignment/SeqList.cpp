#include"SeqList.h"
#include<iostream>
using namespace std;
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
	cout<<endl;
	list->reverse();
	list->listele();
	cout<<endl;
	list->reverse_rec();
	list->listele();
	list->print_sorted(1);

}
