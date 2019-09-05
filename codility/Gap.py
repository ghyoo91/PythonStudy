import math

class Solution:
    def __init__(self, n):
        self.stack = []
        self.result = 0
        while n >= 1:
            tmp = n%2
            self.stack.append(tmp)
            n = math.floor(n/2)

    def calcResult(self):
        flag = 0
        count = 0
        while self.stack:
            tmp = self.stack.pop()
            if tmp == 1:
                if flag == 0:
                    flag = 1
                else:
                    if self.result < count:
                        self.result = count
                    count = 0
            else:
                if flag == 1:
                    count = count+1

    def printSolution(self):
        print(self.result)

a = Solution(1041)
a.calcResult()
a.printSolution()
