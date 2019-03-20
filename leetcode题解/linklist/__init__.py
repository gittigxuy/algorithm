# -*- coding:utf-8 -*- 
__author__ = 'xuy'


data=[1,1,1,2,3,4,5]
count_dict={}
for i in data:
    count_dict[i]=count_dict.get(i,0)+1
print(count_dict[1])