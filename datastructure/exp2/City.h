#ifndef _CITY_H_
#define _CITY_H_
#include<string>
using namespace std;

class City {

public:

    // name of the city
    string name;

    // bookkeeping info
    int	visited;
    int total_fee;
    int total_distance;
    string from_city;

    City() : name(""), visited(0), total_fee(32767), total_distance(0), from_city("") {}

    City(string const &s): name(s), visited(0),
    total_fee(32767), total_distance(0), from_city("") {}}
;

#endif
