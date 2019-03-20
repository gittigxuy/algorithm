# -*- coding:utf-8 -*- 
__author__ = 'xuy'


"""
题目描述：找出相加为sum的若干数据
"""




def my_print(X):
    result=[]
    for i in range(len(X)):
        if X[i]:
            result.append(data_num[i])
    print(result)

#采用递归的方式解决N-sum的问题
#X用来存储最终解，i表示数据的index,X[i]表示是否加入data_num[i]，has表示在加入data_num[i]之前已有的和
#因为会将X[i]={0,1}都遍历一遍，因此时间复杂度是O(2^N)
def enumNumber(X,i,has):
    #判断 是否越界
    if i>=length:
        return
    if has+data_num[i]==sum:
        X[i]=1
        # print(X)
        my_print(X)
        #这里不加X[i]=0也可以，因为后面还是需要 对于X[i]=1赋值
        X[i]=0

    #先假定抽取X[i]，也就是X[i]=1，从而has=has+data_num[i]，
    X[i]=1
    enumNumber(X,i+1,has+data_num[i])
    #然后假定不抽取X[i],也就是X[i]=0,从而has=has,不加上data_num[i]
    X[i]=0
    enumNumber(X,i+1,has)

#这里采用分支界限法进行剪枝，具体解析见pdf
def findNumber(X,i,has,reduce):
    if i>=length:
        return
    if has+data_num[i]==sum:
        X[i]=1
        my_print(X)
        X[i]=0

    #如果list当中所有的元素之和{has+reduce}大于sum,并且{之前数据和+当前数据}<=sum，那么说明可以加上当前值
    elif (has+reduce>=sum) &(has+data_num[i]<=sum):
        X[i]=1
        findNumber(X,i+1,has+data_num[i],reduce-data_num[i])
    #如果不满足加和的条件，也就是，list当中所有的元素和-data_num[i]大于sum，所以总和等于sum是一个不可能的事件
    if (has+reduce-data_num[i]>=sum):
        X[i]=0
        findNumber(X,i+1,has,reduce-data_num[i])


data_num=[1,2,3,4,5]
sum=10
length=len(data_num)

X=[0]*length
#第二个参数表示从第一个元素开始，第三个参数表示初始和为0
#采用递归方式
# enumNumber(X,0,0)

reduce=0
for i in data_num:
    reduce+=i
#采用分支界限法的 递归方式
findNumber(X,0,0,reduce)


