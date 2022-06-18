# https://leetcode.com/problems/find-the-duplicate-number/

# https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?topList=striver-sde-sheet-problems&leftPanelTab=0


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        low, high = 1, len(nums)-1
        
        while low <= high:
            
            currNum = (low + high)//2   # range: [1, n]
            
            countSmallerNumbers = 0
            for num in nums:
                if num <= currNum:
                    countSmallerNumbers += 1
            
            if countSmallerNumbers > currNum:
                RepeatedNum = currNum
                # because we need to find the smallest such number, so
                high = currNum - 1
            else:
                low = currNum + 1
                
        return RepeatedNum
        