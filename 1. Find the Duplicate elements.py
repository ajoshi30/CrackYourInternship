class Solution:
    def findDuplicate(self, nums):
        # Method implementation to find duplicate numbers
        seen = set() # to keep the number you have seen
        for num in nums:
            if num in seen: # to see if the  number seen before or not
                return num # if you have seen the dulipcate number youo can return here
            seen.add(num) # if you have found the uniqu number till that you can add
        return None

