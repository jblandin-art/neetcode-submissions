class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get rid of duplicates
        setNums = set(nums)

        # store the longest so far
        longest = 0

        # iterate through the list
        for num in setNums:
            # if the previous number of the current array integer is not in
            # the array, then this is where a sequence STARTS, initialize length tracker
            # as well as current sequence number tracker. 
            if num - 1 not in setNums:
                currentLength = 1
                currentSequenceNum = num

                # while the current sequence number's next integer is still in our numbers set, 
                while currentSequenceNum + 1 in setNums:
                    # increment the current sequence number, and incremement the current length
                    currentLength += 1
                    currentSequenceNum += 1

                # once the while loop is finally broken, that means the current sequence has
                # ended, save the current longest if larger than longest. 
                longest = max(currentLength, longest)
        
        # return longest
        return longest
