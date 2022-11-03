class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t len_hay = haystack.length();
        size_t len_nee = needle.length();
        
        if (len_nee == 0) {
            return 0;
        }
        else if (len_nee > len_hay) {
            return -1;
        }
        else {
            size_t maximum = len_hay - len_nee + 1;
            for (size_t i = 0; i < maximum; ++i) {
                string haystack_part = haystack.substr(i, len_nee);
                if (haystack_part == needle) {
                    return i;
                }
            }
            return -1;
        }
    }
};