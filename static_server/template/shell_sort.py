#coding:utf-8

def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    #grap = 4
    grap = n//2
    # i = grap
    # for i in range(grap,n):
    #     i = [grap,grap+1,grap+2,grap+3]
    #     while:
    #         if alist[i] < alist[i-grap]:
    #             alist[i],alist[i-grap] = alist[i-grap],alist[i]
    #grap 变化到0之前，插入算法执行到次数
    while grap > 0:
        #插入算法，与普通的插入算法区别就是grap步长；
        for j in range(grap,n):
            # j = [grap,grap+1,grap+2,grap+3]
            i = j
            while i > 0:
                if alist[i] < alist[i-grap]:
                    alist[i],alist[i-grap] = alist[i-grap],alist[i]
                    i -= grap
                else:
                    break
        # 缩短grap步长
        grap //= 2

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)

