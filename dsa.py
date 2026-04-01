"""two sums
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
         

binary search
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

search insert position       
class Solution:
    def searchInsert(self, nums, target):
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

        return l

        move zeroes
        class Solution:
    def moveZeroes(self, nums: List[int]):
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1

        return nums
     
        

        valid palindrome
class Solution:
    def isPalindrome(self, s: str):
        s=s.lower()
        new_s=""
        for i in s:
            if i.isalnum():
                new_s+=i
        
        rev=new_s[::-1]
        return rev==new_s"""

"""selection sort"""
arr = [8,3,-2,1,0,15,2,6]
min=0
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
    print(arr)