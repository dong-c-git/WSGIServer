import sys
sys.setrecursionlimit(1500)

class Findso:
     def __init__(self):
         self.key = "1"
         self.result = 0

     def countFind(self,n):
         if n<1:
             return self.result
         self.result += str(n).count(self.key)
         if n >0:
             self.countFind(n-1)
         return self.result

s = Findso()
for i in range(0,100000):
    print(i)
    print(s.countFind(i))
