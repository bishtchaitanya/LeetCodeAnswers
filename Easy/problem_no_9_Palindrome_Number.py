class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        flag =True
        for i in range(int(len(x)/2)):
            if x[i] == x[-i-1]:
                flag = True
            else:
                flag = False
                break
        return flag
