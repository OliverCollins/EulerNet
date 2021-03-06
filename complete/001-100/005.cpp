//Programmer:    Oliver Collins
//Date:          March 23th, 2016
//Language:      C++

/*
----------------------------------
*/

//Smallest multiple
//Solved

#include <iostream>

using namespace std;

int multiple(int number) {
    int small, divide = 1;
    while (divide != number) {
        if ((small % divide == 0) && (small > divide)) {
            divide++;
        } else {
            divide = 1;
            small++;
        }
    } return small;
}

int main () {
    int number;
    cout << "Select natural number: ";
    cin >> number;
    cout << multiple(number);
    return 0;
}
