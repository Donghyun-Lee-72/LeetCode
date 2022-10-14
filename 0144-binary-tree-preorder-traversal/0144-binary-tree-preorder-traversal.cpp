/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> helper(vector<int> list, TreeNode* root) {
        if (root == nullptr) { return list; }
        else {
            list.push_back(root->val);
        }
        
        list = helper(list, root->left);
        list = helper(list, root->right);
        return list;
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> list;
        list = helper(list, root);
        return list;
    }
};