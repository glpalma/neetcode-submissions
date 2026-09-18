/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean compareDFS(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }

        boolean left = compareDFS(p.left, q.left);
        boolean right = compareDFS(p.right, q.right);

        return p.val == q.val && left && right;
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        return compareDFS(p, q);
    }
}
