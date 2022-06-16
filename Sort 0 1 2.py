# https://www.codingninjas.com/codestudio/problems/sort-0-1-2_631055?topList=striver-sde-sheet-problems&leftPanelTab=0

# https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums
        """
        n = len(nums)
        zero = one = two = 0
        
        for i in range(n):
            if nums[i] == 0:
                zero += 1
            if nums[i] == 1:
                one += 1
            if nums[i] == 2:
                two += 1
                
        for i in range(zero):
            nums[i] = 0
        for j in range(zero, zero+one):
            nums[j] = 1
        for k in range(zero+one, zero+one+two):
            nums[k] = 2
        return nums
        """
        