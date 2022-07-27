Dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
Exp = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = len(s)-1
        ch = ''
        while(i>=0):
            if i == 0:
                num = num+Dict[s[i]]
                break
            ch = s[i-1] + s[i] 
            if ch in Exp:
                num = num + Exp[ch]
                i = i -2

            else:
                num = num + Dict[s[i]]
                i = i-1
        return num 
