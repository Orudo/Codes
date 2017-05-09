#include<iostream>
using namespace std;
class heap
{
public:
	int cont[1000];
	int tail=0;
	int getminlr(int index)
	{
		return cont[index*2+1]<cont[index*2];
	}
	void exchange(int& a,int& b)
	{
		int c=a;
		a=b;
		b=c;
	}
	void insert(int x)
	{
		int index=++tail;
		cont[index]=x;
		while (index!=1)
		{
			if(cont[index]<cont[index/2])
				exchange(cont[index],cont[index/2]);
			index/=2;
		}
	}
	void extract()
	{
		exchange(cont[1],cont[tail]);
		tail--;
		int index=1;
		while (index<=tail/2)
		{
			int next=index*2+getminlr(index);
			clog<<"next"<<next<<endl;
			if(cont[index]>cont[next])
			{
				exchange(cont[index],cont[next]);
				index=next;
			}
			else
				break;
		}
	}
	void list(int index=1)
	{
		//clog<<index<<endl;
		if(index<=tail)
		{
			cout<<cont[index]<<endl;
			list(index*2);
			list(index*2+1);
		}
	}

};

int main()
{
	heap* h=new heap();
	h->insert(3);
	h->insert(5);
	h->insert(6);
	h->insert(2);
	clog<<"list"<<endl;
	h->list();
	h->extract();
	clog<<"list"<<endl;
	h->list();
	return 0;
}
