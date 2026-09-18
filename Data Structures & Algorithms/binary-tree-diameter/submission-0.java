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
    public int depthWithDiameterOnRes(TreeNode root, int[] res) {
        if (root == null) {
            return 0;
        }

        // preciso comparar a solução usando a root e não usando
        
        int left = depthWithDiameterOnRes(root.left, res);
        int right = depthWithDiameterOnRes(root.right, res);

        res[0] = Math.max(res[0], left + right);
        return 1 + Math.max(left, right); // depth
    }

    public int diameterOfBinaryTree(TreeNode root) {
        int[] res = {0};
        depthWithDiameterOnRes(root, res);
        return res[0];
    }
}
