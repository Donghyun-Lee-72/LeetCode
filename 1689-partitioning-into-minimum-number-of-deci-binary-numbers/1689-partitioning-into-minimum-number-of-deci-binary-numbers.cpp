class Solution {
public:
    int minPartitions(string n) {
        int max_num = 0;
        int num;
        for (char const &c : n) {
            num = c - '0';
            max_num = max(max_num, num);
        }
        return max_num;
    }
};