#include "Project2.h"
#include <iostream>
#include <algorithm>
#include <ctime>

/**
 * A Default constructor for the Concert Object. Sets variables to default
 * values.
 **/
Concert::Concert(){
	this->concertName = "Default";
	std::vector<std::string> friends;
	this->friends = friends;
	this->desire = 1;
	std::tm date;
	this->date = date;
}

/**
 * A constructor for the Concert object that accepts all values to set each
 * Concert variable.
 *
 * @param concertName "A string to set the name of the concert"
 * @param friends "A vector of strings that contains a list of friends"
 * @param desire "An integer to determine the desire to attend the concert"
 * @param date "The date of the concert stored in a tm struct"
 **/
Concert::Concert(std::string concertName, std::vector<std::string> friends, int desire, std::tm date){
	this->concertName = concertName;
	this->friends = friends;
	this->desire = desire;
	this->date = date;
  }

/**
 * An operator overloader for < that is used for the std::sort.
 *
 * @param other "A constant Consert reference to be compared to"
 * @return boolean
 **/
bool Concert::operator<(const Concert& other) const {
	if (getDate().tm_year < other.getDate().tm_year)
		return true;
	else if (getDate().tm_year > other.getDate().tm_year)
		return false;
	else if (getDate().tm_mon < other.getDate().tm_mon)
		return true;
	else if (getDate().tm_mon > other.getDate().tm_mon)
		return false;
	else if (getDate().tm_mday < other.getDate().tm_mday)
		return true;
	else if (getDate().tm_mday > other.getDate().tm_mday)
		return false;
	else if (getDesire() > other.getDesire())
		return true;
    	else
		return false;
}

std::ostream& operator<<(std::ostream& os, const Concert& ct)
{
    os << ct.getName() << " " << ct.getDate().tm_mon << "/" <<
      ct.getDate().tm_mday << "/" << ct.getDate().tm_year;
    return os;
}
/**
 * The main function of Project2. This creates 10 objects and sorts them via
 * the std::sort
 *
 * @return integer
 **/
int main() {
	std::vector<std::string> buddies;
	std::tm date1;
	date1.tm_year = 2017;
	date1.tm_mon = 11;
	date1.tm_mday = 13;
	Concert concert1 ("Concert1", buddies, 1, date1);

	std::tm date2;
	date2.tm_year = 2017;
	date2.tm_mon = 10;
	date2.tm_mday = 13;
	Concert concert2 ("Concert2", buddies, 3, date2);

	std::tm date3;
	date3.tm_year = 2017;
	date3.tm_mon = 10;
	date3.tm_mday = 12;
	Concert concert3 ("Concert3", buddies, 2, date3);

	std::tm date4;
	date4.tm_year = 2016;
	date4.tm_mon = 5;
	date4.tm_mday = 22;
	Concert concert4 ("Concert4", buddies, 4, date4);

	std::tm date5;
	date5.tm_year = 2016;
	date5.tm_mon = 5;
	date5.tm_mday = 22;
	Concert concert5 ("Concert5", buddies, 3, date5);

	std::tm date6;
	date6.tm_year = 2017;
	date6.tm_mon = 9;
	date6.tm_mday = 13;
	Concert concert6 ("Concert6", buddies, 1, date6);

	std::tm date7;
	date7.tm_year = 2017;
	date7.tm_mon = 5;
	date7.tm_mday = 13;
	Concert concert7 ("Concert7", buddies, 3, date7);

	std::tm date8;
	date8.tm_year = 2017;
	date8.tm_mon = 5;
	date8.tm_mday = 12;
	Concert concert8 ("Concert8", buddies, 2, date8);

	std::tm date9;
	date9.tm_year = 2017;
	date9.tm_mon = 7;
	date9.tm_mday = 22;
	Concert concert9 ("Concert9", buddies, 4, date9);

	std::tm date10;
	date10.tm_year = 2017;
	date10.tm_mon = 7;
	date10.tm_mday = 22;
	Concert concert10 ("Concert10", buddies, 3, date10);

	std::vector<Concert::Concert> concertList;
	concertList.push_back(concert1);
	concertList.push_back(concert2);
	concertList.push_back(concert3);
	concertList.push_back(concert4);
	concertList.push_back(concert5);
	concertList.push_back(concert6);
	concertList.push_back(concert7);
	concertList.push_back(concert8);
	concertList.push_back(concert9);
	concertList.push_back(concert10);

	std::cout << "Before: \n";
	for (int i = 0; i < concertList.size(); i++){
      std::cout << concertList[i] << "\n";
		//std::cout << concertList[i].getName() << "\n";
	}

	std::sort(concertList.begin(), concertList.end());

	std::cout << "\nAfter: \n";
	for (int i = 0; i < concertList.size(); i++){
      std::cout << concertList[i] << "\n";
		//std::cout << concertList[i].getName() << "\n";
	}

}
