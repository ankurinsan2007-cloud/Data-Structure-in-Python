"""two sums"""
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
         

"""binary search"""
class Solution:
    def search(self, nums, target):
        l=0
        h=len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                h = mid-1

        return -1
        