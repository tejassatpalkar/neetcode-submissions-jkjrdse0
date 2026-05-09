class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        totalNums = set(nums)
        lcsCache = {}
        maxLCS = 0
        for val in totalNums:
            curVal = val
            while curVal in totalNums:
                if curVal in lcsCache:
                    curVal+= lcsCache[curVal]
                else:
                    curVal+=1
                maxLCS = max(maxLCS,curVal-val)
            lcsCache[val] = curVal - val
        
        return maxLCS
                




            



       

        