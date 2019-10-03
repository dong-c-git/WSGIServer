#coding:utf-8

class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkListCycle(object):
    """单向循环链表"""
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0
        #cur游标，用来移动遍历节点
        cur = self.__head
        #count记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        #退出循环，cur指向尾节点，但是节点的元素未打印
        print(cur.elem)

    def add(self,item):
        """在头部添加一个元素，头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self,item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self,pos,item):
        """在指定位置pos添加节点"""
        if pos <=0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            #当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除一个节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None

        while cur.next != self.__head:
            if cur.elem == item:
                #先判断此节点是否是头节点
                if cur == self.__head:
                    #头节点情况 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    #中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                #链表只有一个节点
                self.__head = None
            else:
                #pre.next = cur.next
                pre.next = self.__head

    def search(self,item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False

if __name__ == '__main__':
    ll = SingleLinkListCycle()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.travel()
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()