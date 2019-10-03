#coding:utf-8
class Dueque(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """从队头加入一个item元素"""
        self.__list.insert(0,item)

    def add_rear(self,item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def remove_front(self):
        """从队头删除一个item元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除一个item元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)



if __name__ == '__main__':
    s = Dueque()
    print(s.is_empty())
    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    print(s.is_empty())
    s.add_rear(4)
    print(s.remove_front())
    print(s.remove_front())
    print(s.remove_rear())



