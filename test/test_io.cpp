#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <limits>
// #include <bits/stdc++.h>

using namespace std;

void test_io1() {
    string line, num;
    vector<int> nums;
    stringstream ss;
    int sum = 0;

    cout << "Input nums:" << endl;

    getline(cin, line);
    ss.str(line);

    while (getline(ss, num, ' ')) {
        nums.push_back(stoi(num));
    }

    cout << "Sum(nums): " << endl;

    for (int num : nums) {
        sum += num;
        
    }

    cout << sum << endl;
}

void test_io2() {
    int N, sum = 0;
    string line, num;
    vector<vector<int>> data;
    stringstream ss;

    cout << "Input N: " << endl;
    getline(cin, line);
    N = stoi(line);

    // cin >> N;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "Input data:" << endl;

    for (int i = 0; i < N; ++i) {
        getline(cin, line);
        ss.clear();
        ss.str(line);

        vector<int> nums;

        while(ss >> num) {
            nums.push_back(stoi(num));
        }

        data.push_back(nums);
    }

    for (vector<int> nums : data) {
        for (int num : nums) {
            sum += num;
        }
    }

    cout << "Sum: " << sum << "." << endl;
}

int main() {
    test_io1();

    cout << "*******************************" << endl;

    test_io2();

    return 0;
}