//Programmer:    Oliver Collins
//Date:          March 25th, 2016
//Language:      C++

/*
----------------------------------
*/

//Sum square difference
//Solved

#include <iostream>

using namespace std;

int difference(int number) {
    int sum_squares, natural = 0;
    for (int i = 1; i <= number; i++) {
        sum_squares = sum_squares + (i * i);
    }
    for (int x = 1; x <= number; x++) {
        if (x == number) {
            natural = natural + x;
            natural = natural * natural;
        } else {
            natural = natural + x;
        }
    }
    return (natural - sum_squares);
}

int main () {
    int number;
    cout << "Select natural number: ";
    cin >> number;
    cout << difference(number);
    return 0;
}
