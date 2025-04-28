class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int target = (nums.size()+1) * nums.size() / 2;
        for (int num : nums) {
            target -= num;
        }
        return target;
    }
};