class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        curr = 1 
        a = sorted(nums)
        if len(nums)==0:
            longest = 0
        for i in range(1,len(nums)):
            if a[i] == a[i-1]+1:
                curr+=1
            elif a[i] == a[i-1]:
                curr+=0
            else :
                curr = 1   
            longest = max(longest,curr)
        return longest              

       
       
        