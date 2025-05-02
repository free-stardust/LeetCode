#include <iostream>
#include <stack>

using namespace std;

class MyQueue{
private:
    stack<int> s1, s2;

public:
    void push(int num) {
        s1.push(num);
    }

    int pop() {
        if(s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        } 
        int num = s2.top();
        s2.pop();
        return num;
    }   

    bool empty() {
        if (s1.empty() && s2.empty())
            return true;
        else
            return false;
    }
};

int main() {
    MyQueue q;
    for (int i = 0; i < 5; ++i) {
        q.push(i + 1);
    }
    while (!q.empty()) {
        int num = q.pop();
        cout << num << endl;
    }
    return 0;
}