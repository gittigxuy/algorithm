# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
reference:https://blog.csdn.net/XX_123_1_RJ/article/details/80973518


 Python中的list函数
创建一个list列表:

　　liebiao = list(["参数1","参数2"])

　　liebiao = ["参数1","参数2"]

　　快速创建一个1~9的列表: liebiao = [i for i in range(1,10)]
列表操作方法:

　　list.append(obj)　  　　在列表的末尾添加新的对象

　　list.count(obj)　　  　　统计某个元素在列表中出现的次数

　　list.extend(*obj)　 　　在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)

　　list.index(obj)        　　从列表中找出某个值第一个匹配项的索引位置

　　list.insert(index,obj)　  将对象插入列表,第一个参数可以是位置

　　list.pop(obj=list[-1]　　移除列表中的一个元素(默认最后一个元素),并返回该元素的值

　　list.remove(obj)　　　　移除列表中某个值的第一个匹配项

　　liest.reverse()　　　　　反向列表中的元素

　　list.sort[func]　　　　　对原列表进行排序,参数reverse=True时,从大到小排序

　　list.clear()　　　　　　　清空这个列表(感觉毫无卵用....)

题目描述：返回字符串中最长有效括号长度
eg:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
====================
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

#使用栈方法
def longestValidparentheses1(s):
    stack=[-1]
    res=0
    for i,e in enumerate(s):
        if e=='(':
            stack.append(i)
        elif e==')':
            stack.pop()
            #在pop之后，如果栈为空，那么append当前的index作为右括号的index
            if not stack:
                stack.append(i)
            #如果栈不为空，那么当前的index与栈末的index:stack[-1]的差就是，已经匹配的最大长度
            else:
                res=max(res,i-stack[-1])
    return res

#使用dp方法：
s=')(()'
print(longestValidparentheses1(s))

