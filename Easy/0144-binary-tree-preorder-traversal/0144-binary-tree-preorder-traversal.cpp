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
    void helper(vector<int>& list, TreeNode* root) {
        if (root == nullptr) { return; }
        else {
            list.push_back(root->val);
        }
        
        helper(list, root->left);
        helper(list, root->right);
        return;
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> list;
        helper(list, root);
        return list;
    }
};