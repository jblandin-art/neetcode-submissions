class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # possible consecutive numbers as tuple keys, sequences as values 
        sequences = {}
        # longest has the longest count at index 0 and the sequences key at index 1
        longest = (0, (0, 0))
        # all individual consective numbers in the tuple keys. 
        allKeys = defaultdict(list)
        strictNums = set(nums)
        for num in strictNums:
            #if num == 3:
                #print(allKeys)
            #print("num is:", num)
            if num not in allKeys.keys():
                # update the sequences and allkeys with a new pair of possible consecutive numbers
                sequences[((num - 1), (num + 1))] = [num]
                allKeys[num - 1].append(((num - 1), (num + 1)))
                allKeys[num + 1].append(((num - 1), (num + 1)))
                if longest[0] < 1:
                    longest = (1, (num-1, num+2))
                #print("sequence added", sequences)

            ### MERGE ###
            if len(allKeys[num]) > 1:
                print(sequences)
                #print(allKeys[num], num)
                #print("Pre-merge allKeys: ", allKeys)
                sequences[allKeys[num][0]].extend(sequences[allKeys[num][1]])
                sequences[allKeys[num][0]].append(num)
                maxed = max(sequences[allKeys[num][0]]) + 1
                mined = min(sequences[allKeys[num][0]]) - 1
                sequences[(mined, maxed)] = sequences[allKeys[num][0]]
                oldValue1 = allKeys[num][1]
                oldValue2 = allKeys[num][0]
                del sequences[allKeys[num][1]]
                del sequences[allKeys[num][0]]
                valuesToClear = []
                for oldValue in (oldValue1, oldValue2):
                    for part in oldValue:
                        if part != num:
                            allKeys[part].remove(oldValue)
                for value in valuesToClear:
                    allKeys[value].remove((num, value))
                allKeys[maxed].append((mined, maxed))
                allKeys[mined].append((mined, maxed))
                
                if longest[0] < len(sequences[(mined, maxed)]):
                        longest = (len(sequences[(mined, maxed)]), (mined, maxed))
                #print("\n----MERGED----\n")
                continue
                        
            # if num exists as a possible key then extend the sequence in the sequences array
            # and update keys in sequence array
            for key in allKeys[num]:
                #print(f"Num: {num} is a part of these key tuples: {allKeys[num]}")
                # if consecutive number is added to the end
                if num == max(key):
                    newKey = (min(key), num+1)
                    #print("key is: ", key, "newKey is:", newKey)
                    #print("sequence dictionary:", sequences)
                    sequences[key].append(num)
                    sequences[newKey] = sequences[key]
                    del sequences[key]
                    if longest[0] < len(sequences[newKey]):
                        longest = (len(sequences[newKey]), newKey)
                    allKeys[num+1].append(newKey)
                    # set the matching allKeys pair to be the same as the one
                    # we just changed
                    allKeys[min(key)].remove(key)
                    allKeys[min(key)].append(newKey)
                    #print(f"Num: {num}'s key tuple has now changed to: {allKeys[num+1]}")

                # if consecutive number is added to the beginning
                if num == min(key):
                    newKey = (max(key), num-1)
                    sequences[key].append(num)
                    sequences[newKey] = sequences[key]
                    del sequences[key]
                    if longest[0] < len(sequences[newKey]):
                        longest = (len(sequences[newKey]), newKey)
                    allKeys[num-1].append(newKey)
                    #print(key, allKeys)
                    allKeys[max(key)].remove(key)
                    allKeys[max(key)].append(newKey)
                    #print(f"Num: {num}'s key tuple has now changed to: {allKeys[num-1]}")
                
            del allKeys[num]
        
        # Last task is to merge sequences that should be one. In the current example, [0, -1, -2] should merge with [-4, -3]
        # once the max of one tuple is higher than the min of another, they can merge

        return longest[0]
            
            



