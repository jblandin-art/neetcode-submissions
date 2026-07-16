class Solution:
    # As for time complexity, the reason why this nested while loop inside the for loop
    # doesn't multiply the time complexity, is that the while loop doesn't run for every
    # iteration of the for loop. In fact, it only runs at max n - 1 times. (As many times
    # as there is a neighbor number in the list. 1 sequence of two numbers is one run)

    # Don't just assume nested loops multiply time complexity. Nested loops can and should
    # aspire to run at O(n) instead of O(n^2). They can do so if the inner loop only runs
    # TOTAL, the same amount as the outer loop or less. In this instance, it happens because 
    # once a number is visited in the inner loop, it will no longer make it to the inner loop
    # again in another outer loop iteration. The inner loop only runs at the beginning of 
    # sequences, and gets skipped otherwise. 

    # The if statement before 
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
            # -- GATE KEEP -- #
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
