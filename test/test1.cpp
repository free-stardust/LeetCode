#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int func(string s) {
    int res = 0;
    string sub_s = "";

    for (char c : s) {
        if (sub_s.find(c) == string::npos) {
            sub_s += c;
            res = max(static_cast<int>(sub_s.size()), res);
        }
        else
            sub_s = sub_s.substr(sub_s.find(c) + 1) + c;
    }

    return res;
}

int main(){
    vector<string> ss = {"abcabcbb", "abcabcd", "abcde"};
    for (string s : ss) {
        int res = func(s);
        cout << "Result: " << res << endl;
    }
    return 0;
}