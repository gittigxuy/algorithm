# -*- coding:utf-8 -*- 
__author__ = 'xuy'

class solution:
    def hasPath(self,root,sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val==sum
        new_sum=sum-root.val
        return self.hasPath(root.left,new_sum) or self.hasPath(root.right,new_sum)
-