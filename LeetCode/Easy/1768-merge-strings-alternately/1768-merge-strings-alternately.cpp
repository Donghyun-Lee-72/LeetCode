class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        string result = "";
        
        int i = 0;
        if (len1 < len2) {
            for (i = 0; i < len1; ++i) {
                result.push_back(word1.at(i));
                result.push_back(word2.at(i));
            }
            result.append(word2.substr(len1));
        }
        else {
            for (i = 0; i < len2; ++i) {
                result.push_back(word1.at(i));
                result.push_back(word2.at(i));
            }
            result.append(word1.substr(len2));
        }
        
        return result;
    }
};