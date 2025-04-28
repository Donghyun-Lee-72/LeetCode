#include <queue>

class MyStack {
public:
    std::queue<int> que;
    
    MyStack() {
    }
    
    void push(int x) {
        que.push(x);
    }
    
    int pop() {
        queue<int> temp;
        int len = que.size() - 1;
        for(int i=0; i<len; ++i) {
            temp.push(que.front());
            que.pop();
        }
        int result = que.front();
        que = temp;
        return result;
    }
    
    int top() {
        return que.back();
    }
    
    bool empty() {
        return que.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */