#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>

using namespace std;

string vec2string(vector<int> vec) {
    string s = "[";

    for (int i = 0; i < vec.size(); ++i) {
        if (i < vec.size() - 1)
            s += to_string(vec[i]) + ", ";
        else
            s += to_string(vec[i]);
    }
    
    s += "]";

    return s;
}

void testStack(){
    stack<int> s;
    vector<int> vec1, vec2;

    for (int i = 0; i < 10; ++i) {
        s.push(i);
        vec1.push_back(i);
    }

    while (!s.empty()) {
        vec2.push_back(s.top());
        s.pop();
    }

    cout << "Stack push: " << vec2string(vec1) << endl;
    cout << "Stack pop: " << vec2string(vec2) << endl; 
}


void testQueue() {
    queue<int> q;
    vector<int> vec1, vec2;

    for (int i = 0; i < 5; ++i) {
        q.push(i);
        vec1.push_back(i);
    }

    while (!q.empty()){
        vec2.push_back(q.front());
        q.pop();
    }   

    cout << "Queue push: " << vec2string(vec1) << endl;
    cout << "Queue pop: " << vec2string(vec2) << endl;
}

void testDeque() {
    deque<int> dq;
    vector<int> vec1, vec2;

    for (int i = 0; i < 8; ++i) {
        if (i % 2 == 0) 
            dq.push_back(i);
        else
            dq.push_front(i);
    }

    dq.insert(dq.begin() + 3, 999);

    for (int i = 0; i < dq.size(); ++i) {
        vec1.push_back(dq[i]);
    }

    dq.erase(dq.cbegin() + 3);

    while (!dq.empty()) {
        vec2.push_back(dq.front());
        dq.pop_front();
    }

    cout << "Deque push: " << vec2string(vec1) << endl;
    cout << "Deque pop: " << vec2string(vec2) << endl;
}

int main(){
    testStack();
    cout << "**********************************************" << endl;
    testQueue();
    cout << "**********************************************" << endl;
    testDeque();
    cout << stoi("2") << endl;
    return 0;
}