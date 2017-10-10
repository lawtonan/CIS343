#ifndef CONCERT_H
#define CONCERT_H
#include <string>
#include <vector>
#include <ctime>
class Concert {
// Who will be performing?
std::string concertName;

// A list of the people you want to take with you.  May be empty or
// arbitrarily full.
std::vector<std::string> friends;

// A value from 1-10 concerning how badly you want to see this show.
int desire;

// The date of the show (See http://en.cppreference.com/w/cpp/chrono/c/tm)
std::tm date;
public:
Concert();
Concert(std::string, std::vector<std::string>, int, std::tm);
bool operator<(const Concert& other) const;
int getDesire() const {return desire;}
std::tm getDate() const {return date;}
std::string getName() const {return concertName;}
friend std::ostream& operator<<(std::ostream& os, const Concert& ct);
};

#endif
