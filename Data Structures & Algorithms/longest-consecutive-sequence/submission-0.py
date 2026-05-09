class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        totalNums = set(nums)
        maxLCS = 0
        for val in totalNums:
            curVal = val
            while curVal in totalNums:
                curVal+=1
                maxLCS = max(maxLCS,curVal-val)
        
        return maxLCS
                




            



       

        