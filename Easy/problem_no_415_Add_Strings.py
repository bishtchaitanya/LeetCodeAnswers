def convertToInt(num):
        intS = [0,1,2,3,4,5,6,7,8,9]
        temp = 0
        for i in range(len(num)):
            tens = 10**(i)
            for j in intS:
                if num[-1-i] == str(j):
                    temp = temp + j*tens
        return temp

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = convertToInt(num1)
        num2 = convertToInt(num2)
        sum = num1 + num2
        return str(sum)
