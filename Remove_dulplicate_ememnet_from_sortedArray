class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize the index for the next unique element
        k = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous one
            if nums[i] != nums[i - 1]:
                # Place it at the index of the next unique element
                nums[k] = nums[i]
                # Increment the index
                k += 1
        
        return k
