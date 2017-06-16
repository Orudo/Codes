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
			cout<<"arriving : "<< eve.getjob().getnumpages()<<" pages from "<<eve.getjob().getuser()<<" at "<<cnt<<endl;
			if(eta.empty())
			{eta.push(cnt+eve.getjob().getnumpages()*seconds_per_page);cout<<" serving : "<< eve.getjob().getnumpages()<<" pages from "<<eve.getjob().getuser()<<" at "<<cnt<<endl;}
			else eta.push(eta.back()+eve.getjob().getnumpages()*seconds_per_page);
			workload.pop();
			
		}
		//clog<<"mark"<<endl;
		if(!processing.empty()&&cnt==eta.front())
		{
			processing.pop();
			eta.pop();
			if(!processing.empty()){
				event eve=processing.front();
				cout<<"serving : "<< eve.getjob().getnumpages()<<" pages from "<<eve.getjob().getuser()<<" at "<<cnt<<endl;
				
				//clog<<processing.front().arrival_time()<<" "<<cnt-processing.front().arrival_time()<<endl;
				latency+=cnt-processing.front().arrival_time();
			}
			//processing.pop();
			//eta.pop();
		}
		cnt++;

			

	}
	clog<<"All latency:"<<latency<<endl<<"average latency:"<<(float)latency/jobs<<endl<<"job counts:"<<jobs<<endl;
	
}

fifo::fifo(int second_per_second):simulator(second_per_second)
{
	cnt=0;
	latency=0;
//	super(second_per_second);
}
