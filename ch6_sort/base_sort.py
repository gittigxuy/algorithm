# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
排序的基本操作:
稳定的排序：冒泡{BubbleSort}，插入{insertSort}，归并{mergesort}；是稳定的排序
reference:https://www.cnblogs.com/MrFiona/p/5978491.html
实现了６大排序算法，其中重点是堆排序和快排

topK问题使用小顶堆，reference:https://www.cnblogs.com/qlky/p/7512199.html
"""

####
def insertsort(data,num_data):
    """
    描述:最终排序结果是一个非降序{升序}的list，时间复杂度是O(N^2)
    插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n ^ 2)。
    是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），
    而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中
    """
    for i in range(1,num_data):
        #从第二个元素开始，待插入的数据是key
        key=data[i]
        j=i-1
        while j>=0:
            #找到了插入位置，元素向后移动
            if data[j]>key:
                data[j+1]=data[j]
                data[j]=key
            j-=1

    return data
##########
def bubble_sort(data,num_data):
    '''
    描述:从小到大排序,时间复杂度是O(N^2)
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误{前面的数据大于后面的数据，即list[i]>list[j]}就把他们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    '''
    for i in  range(num_data):
        for j in range(i+1,num_data):
            if data[i]>data[j]:
                data[j],data[i]=data[i],data[j]
    return data
###########
def select_sort(data,num_data):
    '''
    描述:从小到大排序,时间复杂度是O(N^2)
    基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
    '''
    for i in range(num_data):
        #选出待定最小的元素
        min=i
        for j in range(i+1,num_data):
            if data[min]>data[j]:
                min=j
        data[min],data[i]=data[i],data[min]

    return data
###########
def quicksort(data,left,right):
    '''
    描述:时间复杂度是O(NlogN)
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
    '''
    if left >= right:
        return data
    #设置一个阈值，先假定这个阈值是第一个元素，如果最右面的元素大于key，那么进行交换，否则最右面的元素index-=1
    key = data[left]

    #low和high是不变量，left和right是index指针变量
    low = left
    high = right
    while left < right:
        while left < right and data[right] >= key:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= key:
            left += 1
        data[right] = data[left]
    #此时left=right，所以data[left]=data[right]，此时data[right]作为划分点
    data[right] = key
    quicksort(data, low, left - 1)
    quicksort(data, left + 1, high)
    #返回排序之后的数据
    return data
##############################

def QuickSort(input_list, left, right):
    '''
    函数说明:快速排序（升序）
    Author:
        www.cuijiahua.com
    Parameters:
        input_list - 待排序列表
    Returns:
        无
    '''
    #快排的division思想
    def division(input_list, left, right):
        '''
        函数说明:根据left和right进行一次扫描，重新找到基准数
        Author:
            www.cuijiahua.com
        Parameters:
            input_list - 待排序列表
            left - 左指针位置
            right - 右指针位置
        Returns:
            left - 新的基准数位置
        '''
        base = input_list[left]
        while left < right:
            while left < right and input_list[right] >= base:
                right -= 1
            input_list[left] = input_list[right]
            while left < right and input_list[left] <= base:
                left += 1
            input_list[right] = input_list[left]
        input_list[left] = base
        #返回划分点
        return left

    if left < right:
        base_index = division(input_list, left, right)
        QuickSort(input_list, left, base_index - 1)
        QuickSort(input_list, base_index + 1, right)
    return input_list


######################
#小顶堆排序，从大到小进行排序
def little_heap_sort(data,num_data):
    """
        描述:从大到小进行小顶堆排序，时间复杂度O（NlogN）,是不稳定的排序
        堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。
        堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
        在数组的非升序排序中，需要使用的就是小根堆，因为根据小根堆的要求可知，最小的值一定在堆顶。
    """
    # step1:建堆
    #　step2:堆顶与叶子节点交换
    #step3:调整堆结构

    # 创建堆
    little_build_heap(data, num_data)
    # 顺序颠倒，从num_data~0开始遍历
    for i in range(0, num_data)[::-1]:
    # for i in range(num_data-1,-1,-1):
        # swap(data[i],data[0])
        data[i], data[0] = data[0], data[i]
        #调整堆结构
        little_adjust_heap(data, 0, i)
    return data

def little_build_heap(data,num_data):
    for i in range(0,num_data//2)[::-1]:
        little_adjust_heap(data,i,num_data)
def little_adjust_heap(data,i,num_data):

    #k的孩子节点的index
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    min = i
    if i < num_data // 2:

        #fix，大顶堆是data[lchild]>data[min]
        if lchild < num_data and data[lchild] <= data[min]:
            min = lchild
        if rchild < num_data and data[rchild] <= data[min]:
            min = rchild
        #进行交换index,然后调整堆结构
        if min != i:
            data[min], data[i] = data[i], data[min]
            little_adjust_heap(data, min, num_data)
##############
# 大顶堆排序
def  big_heap_sort(data,num_data):
    """
    描述:从小到大进行大顶堆排序，时间复杂度O（NlogN）,是不稳定的排序
    堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。
    堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
    在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
    """

    #创建堆,
    big_build_heap(data,num_data)
    #顺序颠倒，从num_data~0开始遍历，遍历的时间复杂度是O(N)
    for i in range(0,num_data)[::-1]:
        #swap(data[i],data[0])
        data[i],data[0]=data[0],data[i]
        #时间复杂度是O(logN),也就是树的深度
        big_adjust_heap(data,0,i)
    return data

def big_build_heap(data,num_data):
    #从(size/2)-1开始遍历，一直到0
    # 构建堆是从下到上，因此需要逆序,最终将最大的元素放到堆顶
    for i in range(0,num_data//2)[::-1]:
        big_adjust_heap(data,i,num_data)

# 调整堆结构是从上到下
def big_adjust_heap(data,i,num_data):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < num_data // 2:
        if lchild < num_data and data[lchild] > data[max]:
            max = lchild
        if rchild < num_data and data[rchild] > data[max]:
            max = rchild
        #进行交换index,然后调整堆结构
        if max != i:
            #swap
            data[max], data[i] = data[i], data[max]

            big_adjust_heap(data, max, num_data)

#大顶堆排序，从小到大排序
def heap_sort(data):
    import heapq
    h=[]
    for i in data:
        heapq.heappush(h,i)
    return [heapq.heappop(h) for i in range(len(h))]

###############
#归并排序

#合并操作的时间复杂度是O(N)
def merge(left,right):
    #合并过程
    i,j=0,0
    #新创建了一个空间复杂度为O(N)的变量
    result=[]
    #i表示左半部分的index，j是右半部分的index
    while i<len(left) and  j<len(right):
        #从小到大排序
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 将左半部分或者有右部分的剩余的数据放到result当中
    result.extend(left[i:])
    result.extend(right[j:])
    return result



def merge_sort(lists):
    '''
        描述（利用递归）,空间复杂度是O（N）,时间复杂度是 O(NlogN)
        归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；
        即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
        归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，
        并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。归并排序的算法我们通常用递归实现，
        先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。
    '''
    if len(lists) <= 1:
        return lists
    mid = len(lists) // 2
    #这里的递归的时间复杂度是O(NlogN),具体推导见pdf
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    #合并左列表，右列表
    return merge(left, right)

# def merge1(left,right):
#
# def merge_sort1(lists,low,high):
#     if len(lists)<=1:
#         return lists
#     mid=(low+high)//2
#     left=merge_sort1(lists,low,mid)
#     right=merge_sort1(lists,mid+1,high)
#     return merge1(left,right)
##############

#测试代码
li=[3,2,4,5,1,4,10]
# print(QuickSort(li,0,len(li)-1))
# print(heap_sort(li))#调用heapq包
# print(insertsort(li,len(li)))
# print(bubble_sort(li,len(li)))
# print(select_sort(li,len(li)))
# print(quicksort(li,0,len(li)-1))
print(big_heap_sort(li,len(li)))
# print(little_heap_sort(li,len(li)))

# print(merge_sort(li))

