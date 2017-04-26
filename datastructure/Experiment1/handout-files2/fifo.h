#ifndef _FIFO_H_ 
#define _FIFO_H_

#include"simulator.h"
#include<string>
#include<queue>
#include"event.h"

class fifo: public simulator
{
	private:
		queue<event> processing;
		queue<int> eta;
		int cnt,latency,jobs;
	public:
		void simulate(std::string file);
		fifo(int second_per_paper);//:simulator(second_per_paper);
	
};


#endif
