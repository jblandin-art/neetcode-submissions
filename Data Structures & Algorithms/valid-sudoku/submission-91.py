class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n)
        def alldiff(nums):
            if len(nums) == 0:
                return True
            hashmap = defaultdict(int)
            for num in nums:
                hashmap[num] += 1
            del hashmap['.']
            for value in hashmap.values():
                if value > 1:
                    return False
            return True
        
        # check if row is alldiff
        # O(n^2)
        for row in board:
            if alldiff(row) == False:
                print("row failed", row)
                return False
        # check if column is alldiff
        # O(n^2)
        column = []
        for c in range(len(board)):
            for r in range(len(board)):
                column.append(board[r][c])
            print(column)
            if alldiff(column) == False:
                print("column failed", row)
                return False
            column = []

        # check if square is alldiff
        # O (n^2)
        square = []
        for c in range(len(board) // 3):
            for r in range(len(board)):
                if (r % 3 + c*3) % 3 == 0:
                    # alldiff here is capped at square size 9
                    # it does not grow with input size so is treated as
                    # constant time in this instance
                    print("this box was checked")
                    if alldiff(square) == False:
                        print("square failed", row)
                        return False 
                    square = []
                    print("switch")
                #print(r % 3 + c*3)
                print(r)
                square.extend(board[r % 3 + c*3][r // 3 * 3:r // 3 * 3 + 3])
                print("board square", square)
            if c == (len(board) // 3) - 1:
                print("this box was checked")
                if alldiff(square) == False:
                    print("square failed", row)
                    return False 
                square = []
                print("switch")

        
        # change this back to True. It should return
        # True if it makes it past all the 
        # Test cases above. 
        return True
    
