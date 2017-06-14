#pragma warning (disable:4786)
#pragma warning (disable:4503)
#include <set>
#include "RailSystem.h"

void RailSystem::reset(void) {

    // TODO: reset the data objects of the 
    // City objects' contained in cities
    
}

RailSystem::RailSystem(string const &filename) {
    
    load_services(filename);
}

void RailSystem::load_services(string const &filename) {

	ifstream inf(filename.c_str());
	string from, to;
	int fee, distance;

	while ( inf.good() ) {

		// Read in the from city, to city, the fee, and distance.
		inf >> from >> to >> fee >> distance;

		if ( inf.good() ) {
			City city;
			if(cities.find(from)!=cities.end())
			{
				outgoing_services.find(from)->second.push_front(new Service(to,fee,distance));
				//clog<<"input: outgoing "<<outgoing_services.find(from)->second
				for(list<Service*>::iterator it=outgoing_services.find(from)->second.begin();it!=outgoing_services.find(from)->second.end();it++)
					clog<<"input:iter:"<<from<<":"<<(*it)->destination<<" fee:"<<(*it)->fee<<endl;
			}else{
				cities.insert(std::pair<string,City*>(from,new City(from)));
				list<Service*> serv;
				serv.push_front(new Service(to,fee,distance));
				outgoing_services.insert(std::pair<string,list<Service*> > (from,serv));
				//std::clog<< outgoing_services.find(from)->second.front()->destination <<std::endl;
			}
			// TODO: Add entries in the cities container and
			// and services in the rail system for the new 
            // cities we read in.	

		}
	}
	
	inf.close();
}

RailSystem::~RailSystem(void) {

    // TODO: release all the City* and Service*
    // from cities and outgoing_services

}

void RailSystem::output_cheapest_route(const string& from,
                const string& to, ostream& out) {

	reset();
	pair<int, int> totals = calc_route(from, to);

	if (totals.first == INT_MAX) {
		out << "There is no route from " << from << " to " << to << "\n";
	} else {
		out << "The cheapest route from " << from << " to " << to << "\n";
		out << "costs " << totals.first << " euros and spans " << totals.second
			<< " kilometers\n";
        cout << recover_route(to) << "\n\n";
	}
}

bool RailSystem::is_valid_city(const string& name) {

	return cities.count(name) == 1;
}
void RailSystem::Cityinit(){
	for (map<string,City*>::iterator it=cities.begin();it!=cities.end();it++)
	{
		it->second->total_distance=0;
		it->second->total_fee=32767;
		it->second->visited=0;
	}
}
pair<int, int> RailSystem::calc_route(string from, string to) {
	Cityinit();
	priority_queue<City*, vector<City*>, Cheapest> candidates;
	set<City*> cityset;
	int num_cities=cities.size();
	//candidates.push(from);
	candidates.push(cities.find(from)->second);
	cities.find(from)->second->visited++;
			cities.find(from)->second->total_fee=0;
	cityset.insert(cities.find(from)->second);
	while(!candidates.empty())
	{
		City* city=candidates.top();
		cityset.erase(city);
		candidates.pop();
		clog<<city->name<<" total fee: "<<city->total_fee<<endl;
		list<Service*> out_serv=outgoing_services.find(city->name)->second;
		for(std::list<Service*>::iterator it=out_serv.begin();it!=out_serv.end();++it)
		{
			City* des=cities.find((*it)->destination)->second;
			clog<<"des:"<<des->name<<" des total:"<<des->total_fee<<endl;
			if(des->visited>num_cities)  return pair<int,int>(0,0);
			if(city->total_fee+(*it)->fee<des->total_fee)
			{
				clog<<"des update:"<<des->name<<" fee:"<<city->total_fee+(*it)->fee<<endl;
				des->total_fee=city->total_fee+(*it)->fee;
				des->total_distance=city->total_distance+(*it)->distance;
				clog<<"des update:"<<des->total_fee<<endl;
				des->from_city=city->name;
				if(cityset.find(des)==cityset.end())
					candidates.push(des);
				else clog<<"block"<<endl;
				des->visited++;
			}
		}
	}
    // TODO: Implement Dijkstra's shortest path algorithm to
    // find the cheapest route between the cities
    

	// Return the total fee and total distance.
	// Return (INT_MAX, INT_MAX) if not path is found.
	if (cities[to]->visited) {
		return pair<int,int>(cities[to]->total_fee, cities[to]->total_distance);
	} else {
		return pair<int,int>(INT_MAX, INT_MAX);
 	}
	 return pair<int,int>(0,0);

}

string RailSystem::recover_route(const string& city) {
	City* current=cities.find(city)->second;
	string path=current->name;
	do
	{
		path=current->from_city+"->"+path;
		current=cities.find(current->from_city)->second;
	}while(current->from_city!="");

	// TODO: walk backwards through the cities
	// container to recover the route we found

	return path;
}
