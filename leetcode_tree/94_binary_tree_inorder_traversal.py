# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def inorder_util(self, root: TreeNode, result: List):
        if root:
            self.inorder_util(root.left, result)
            result.append(root.val)
            self.inorder_util(root.right, result)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.inorder_util(root, result)
        return result
