# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
二叉查找树
"""


class TreeNode:
    def __init__(self, val):
        self.val = val;
        self.left = None;
        self.right = None;


def insert(root, val):
    if root is None:
        root = TreeNode(val);
    else:
        if val < root.val:
            root.left = insert(root.left, val);  # 递归地插入元素
        elif val > root.val:
            root.right = insert(root.right, val);
    return root;


def query_recursion(root, val):
    if root is None:
        return;
    if root.val is val:
        return 1;
    if root.val < val:
        return query_recursion(root.right, val)  # 递归地查询
    else:
        return query_recursion(root.left, val)






def findmin(root):
    if root.left:
        return findmin(root.left);
    else:
        return root;


def delnum(root, val):
    if root is None:
        return;
    if val < root.val:
        return delnum(root.left, val);
    elif val > root.val:
        return delnum(root.right, val);
    else:  # 删除要区分左右孩子是否为空的情况
        if (root.left and root.right):

            tmp = findmin(root.right);  # 找到后继结点
            root.val = tmp.val;
            root.right = delnum(root.right, val);  # 实际删除的是这个后继结点

        else:
            if root.left is None:
                root = root.right;
            elif root.right is None:
                root = root.left;
    return root;


# 測试代码
root = TreeNode(3);
root = insert(root, 2);
root = insert(root, 1);
root = insert(root, 4);

# print query(root,3);
print (query_recursion(root, 1))
root = delnum(root, 1)
print (query_recursion(root, 1))