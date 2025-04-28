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
    int kthSmallest(TreeNode* root, int k) {
        TreeNode* curr = root;
        stack<TreeNode*> stack;
        while (k > 0) {
            if (curr != nullptr) {
                stack.push(curr);
                curr = curr->left;
            } else if (!stack.empty()) {
                curr = stack.top();
                stack.pop();
                --k;
                if (k == 0) {
                    return curr->val;
                } else {
                    curr = curr->right;
                }
            }
        }
        
        return curr->val;
    }
};