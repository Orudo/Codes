#pragma warning (disable:4786)
#pragma warning (disable:4503)

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

pair<int, int> RailSystem::calc_route(string from, string to) {

	priority_queue<City*, vector<City*>, Cheapest> candidates;
	int num_cities=cities.size();
	//candidates.push(from);
	candidates.push(cities.find(from)->second);
	cities.find(from)->second->visited++;
	while(!candidates.empty())
	{
		City* city=candidates.front();
		city->total_fee=0;
		candidates.pop();
		list<Service*> out_serv=outgoing_services.find(from)->second;
		for(std::list<Service*>::iterator it=out_serv.begin;it!=out_serv.end();++it)
		{
			City* des=cities.find(it->destination)->second;
			if(des->visited>num_cities)  return pair<int,int>(0,0);
			if(city->total_fee+it->fee<des->total_fee)
			{
				des->total_fee=city->total_fee+it->fee;
				candidates.push(des);
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
	
	// TODO: walk backwards through the cities
	// container to recover the route we found

	return "";
}
int main(){
	RailSystem rs("services.txt");
	return 0;
}
