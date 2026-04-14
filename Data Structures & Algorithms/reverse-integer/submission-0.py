class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        isNeg = x < 0
        if isNeg:
            x*=-1
        while x != 0:
            temp = x % 10 
            y = y * 10
            y +=temp
            if y & (~0xFFFFFFFF) != 0:
                return 0
            x = x // 10 
        if isNeg:
            y = y  * -1 
        return y
        