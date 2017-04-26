#include"fifo.h"
#include<iostream>
using namespace std;

void fifo::simulate(std::string file)
{
	loadworkload(file);
	jobs=workload.size();
	/*for (int i=0;!workload.empty();i++)
	{
		clog<<workload.front()<<endl;
		workload.pop();
	}*/
	while (!workload.empty()||!processing.empty())
	{
		//clog<<workload.front()<<endl;
		while(!workload.empty()&&cnt==workload.front().arrival_time())
		{
			//clog<<"poping"<<endl;
			event eve=workload.front();
			processing.push(eve);
			cout<<"arriving at"<<cnt<<" pages "<< eve.getjob().getnumpages()<<endl;
			if(eta.empty())
			{eta.push(cnt+eve.getjob().getnumpages()*seconds_per_page);cout<<"serving at"<<cnt<<endl;}
			else eta.push(eta.back()+eve.getjob().getnumpages()*seconds_per_page);
			workload.pop();
			
		}
		//clog<<"mark"<<endl;
		if(!processing.empty()&&cnt==eta.front())
		{
			processing.pop();
			eta.pop();
			if(!processing.empty()){
				cout<<"serving at "<<cnt<<endl;
				
				clog<<processing.front().arrival_time()<<" "<<cnt-processing.front().arrival_time()<<endl;
				latency+=cnt-processing.front().arrival_time();
			}
			//processing.pop();
			//eta.pop();
		}
		cnt++;

			

	}
	clog<<latency<<endl<<(float)latency/jobs<<endl<<jobs<<endl;
	
}

fifo::fifo(int second_per_second):simulator(second_per_second)
{
	cnt=0;
	latency=0;
//	super(second_per_second);
}
