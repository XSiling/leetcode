# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    post_order_stack = []

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        for i in range(len(postorder)):
            self.post_order_stack.append(postorder[i])

        
        last = postorder[-1]
        index_inorder = inorder.index(last)

        self.post_order_stack.pop()

        left_inorder = inorder[0:index_inorder]
        right_inorder = inorder[index_inorder+1:]
        
        left_root = self.constructRoot(left_inorder, postorder)
        right_root = self.constructRoot(right_inorder, postorder)
        root = TreeNode(postorder[-1], left_root, right_root)

        return root
    
    def constructRoot(self, inorder, postorder):
        if len(inorder) == 1:
            return TreeNode(inorder[0], None, None)
        
        if len(inorder) == 0:
            return None

        # max_postorder_index = -1
        # max_inorder_index = -1

        # for i in range(len(inorder)):
        #     postorder_index = postorder.index(inorder[i])
        #     if postorder_index > max_postorder_index:
        #         max_postorder_index = postorder_index
        #         max_inorder_index = i

        for i in range(len(self.post_order_stack)):
            if self.post_order_stack[len(self.post_order_stack) - i -1] in inorder:
                max_inorder_index = inorder.index(self.post_order_stack[len(self.post_order_stack) - i -1])
                self.post_order_stack.pop(len(self.post_order_stack) - i -1)
                break
            

        left_inorder = inorder[0:max_inorder_index]
        right_inorder = inorder[max_inorder_index+1:]

        left_root = self.constructRoot(left_inorder, postorder)
        right_root = self.constructRoot(right_inorder, postorder)

        root = TreeNode(inorder[max_inorder_index], left_root, right_root)
        return root





