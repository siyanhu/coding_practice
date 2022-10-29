# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        stack = []

        while root or stack:
            while root:
                out.append(root.val)
                stack.append(root)
                root = root.left
            node = stack.pop()
            root = node.right

        return out


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # def preOrder(node, results):
        #     if node:
        #         results.append(node.val)
        #         preOrder(node.left, results)
        #         preOrder(node.right, results)
        #
        # results = []
        # preOrder(root, results)
        # return results

        def inorder(node, result_list):
            if node:
                inorder(node.left, result_list)
                inorder(node.right, result_list)
                result_list.append(node.val)

        rslt = list()
        inorder(root, rslt)
        return rslt