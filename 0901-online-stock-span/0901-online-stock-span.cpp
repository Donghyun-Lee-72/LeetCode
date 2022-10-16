class StockSpanner {
public: 
    std::vector<int> history;
    
    StockSpanner() {
        
    }
    
    int next(int price) {
        history.push_back(price);
        
        for(auto iter=history.rbegin(); iter != history.rend(); ++iter) {
            if (*iter > price) {
                return std::distance(history.rbegin(), iter);
            }
        }
        return history.size();
    }
        
        // auto result = std::find_if(history.rbegin(), history.rend(),
        //                            [](int i, int price) { return i > price; });
        // return std::distance(result, history.rbegin());
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */