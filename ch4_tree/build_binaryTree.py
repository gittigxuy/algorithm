# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
先序初始化二叉树，中序遍历
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def build_tree(self,root,layer):
        # 递归的返回条件
        if not root:
            return
        for i in range(layer):
            print('----')
        print(root.val)
        self.build_tree(root.left,layer+1)
        self.build_tree(root.left,layer+1)


# def init_binaryTree():
#     root=TreeNode(1)
#     root.left=TreeNode(2)
#     root.right=TreeNode(3)
#     root.left.left=TreeNode(4)
#
#     return root
#
# solu=solution()
# root=init_binaryTree()
# solu.build_tree(root,2)


def insert(root,val):
    if not root:
        return TreeNode(val)
    if val<=root.val:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root

# 先序初始化二叉树
def init_binaryTree(data):
    root=None
    for i in data:
        root=insert(root,i)
    return root

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)

data=[5,3,1,4,7,6]
root=init_binaryTree(data)
in_order(root)

