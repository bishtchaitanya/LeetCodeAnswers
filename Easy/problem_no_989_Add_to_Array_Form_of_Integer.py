class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = 0
        for i in range(len(num)):
            tens = 10**(i)
            temp = temp + num[-i-1]*tens
        temp = temp + k
        temp = str(temp)
        num = []
        for i in range(len(temp)):
            num.append(int(temp[i]))
        return num
