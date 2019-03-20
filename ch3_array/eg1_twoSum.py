# -*- coding:utf-8 -*- 
__author__ = 'xuy'

num_data=[3,2,4]
# leetcode1
sum=6
#不能解决乱序问题,仅仅输出了符合two-sum的内容
def twoSum(num_data,sum):
    length = len(num_data)
    start=0
    end=length-1

    while(start<end):
        cur_sum=num_data[start]+num_data[end]
        if cur_sum==sum:
            print("%d %d"%(num_data[start],num_data[end]))
            break
        else:
            if cur_sum<sum:
                start+=1
            else:
                end-=1




#解决乱序问题：先进行排序
# 时间复杂度O(NlongN+N),空间复杂度O(1)
#采用双指针的方法
def twoSum1(num_data,sum):
    index=[]
    length = len(num_data)
    #复制原来的list
    numtosort=num_data[:]
    #对于原来的list进行排序
    numtosort.sort()
    start=0
    end=length-1
    while start<end:
        cur_sum=numtosort[start]+numtosort[end]
        if cur_sum==sum:
            for k in range(length):
                # 存储下标
                if num_data[k]==numtosort[start]:
                    #插入起始位置index
                    index.append(k)
                    break
            #将k置为0，重新从头扫描
            k=0
            for k in range(length):
                if num_data[k]==numtosort[end]:
                    #插入结束的位置index
                    index.append(k)
                    break
            index.sort()
            break
        else:
            if cur_sum<sum:
                start+=1
            else:
                end-=1
    # 计数从第一个开始计数，因此需要加上１
    return (index[0]+1,index[1]+1)
# twoSum1(num_data,sum)
# 时间复杂度O(N),空间复杂度O(N)
def twoSum2(num_data,sum):
    #这里dict[data]=index，也就是dict的key存储的是实际的数据，dict的 value存储的是下标
    dict={}
    for i in range(len(num_data)):
        x=num_data[i]
        #计算剩余的另一个数字
        if sum-x in dict:
            return [dict[sum-x]+1,i+1]
        dict[x]=i

print(twoSum2(num_data,sum))





