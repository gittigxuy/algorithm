# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""

reference:https://blog.csdn.net/qq_21815981/article/details/79833976
这里进行一下说明：
while head和while head.next的区别：
while head是执行完该尾节点之后退出循环，因此最后head指向None
while head.next没有执行该尾部节点退出循环，因此最后head指向尾部节点
"""

class LinkNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def has_cycle(self,head):
        if head==None:
            return
        fast,slow=head,head
        while fast.next.next and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    """
    判断有序链表中的中位数
    如果总的链表长度为奇数，那么直接返回慢指针的元素即可
    如果总的链表长度为偶数，那么返回上中位数＋下中位数的平均值
    """
    def middle_num(self,head):
        if head is None:
            return
        fast,slow=head,head


        while fast and slow:
            # 到达最后一个节点，那么slow指针所指的位置就是中间链表
            if fast.next is None:
                return slow.val
            # fast到达倒数第二个节点，那么返回的结果应该是slow以及slow.next的平均值
            elif fast.next is not None and fast.next.next is None:
                return (slow.val+slow.next.val)/2
            else:
                fast=fast.next.next
                slow=slow.next

    """
    输出倒数第k个链表,只需要将慢指针指向从前往后数第k-1个即可，此时慢指针　指向从后往前数第k个值
    只需要将快指针和慢指针相差k-1就可以了，当快指针移动到链表的最后节点的时候
    由于两个指针的距离保持在k-1，当第一个指针到达链表的尾节点时候，第二个指针正好是倒数第K个节点，
    """
    def findlastK(self,head,k):
        if head is None:
            return
        fast,slow=head,head
        # 快指针先移动k-1个链表节点
        for i in range(k-1):
            fast=fast.next
        # 直到fast指针指向最后节点
        while fast.next:
            # 快慢指针一起移动
            fast=fast.next
            slow=slow.next
        return slow.val
    """
    判断环入口
    step1:判断是否有环
    step2:判断环入口
    """
    def find_cycle_start(self,head):
        if head is None:
            return
        fast,slow=head,head
        while fast and slow:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        # 如果二者当中有一个遍历完链表之后，还没碰上，那么说明没有环
        if fast is None or slow is None:
            return None
        #ｓｔｅｐ２：找到环入口
        slow=head#让slow回到链表的起点，fast留在相遇点,两个指针一起移动
        while slow!=fast:#当slow和fast再次相遇时，那个点就是环的入口点
            slow=slow.next
            fast=fast.next
        return slow.val


def init_linklist_has_cycle(data,num_data):
    head=LinkNode(None)
    point=head
    for i in range(num_data):
        point.next=LinkNode(data[i])
        point=point.next
    # 形成环
    point.next=head
    return head.next
def init_linklist(data,num_data):
    head = LinkNode(None)
    point = head
    for i in range(num_data):
        point.next = LinkNode(data[i])
        point = point.next
    # 形成环
    # point.next = head
    return head.next

if __name__=='__main__':
    solu=Solution()
    data=[1,2,3,4,5,6]
    head=init_linklist_has_cycle(data,len(data))
    result=solu.has_cycle(head)
    # result=solu.middle_num(head)
    # result=solu.findlastK(head,4)
    # result=solu.find_cycle_start(head)
    print (result)
