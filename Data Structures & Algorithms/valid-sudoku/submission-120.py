class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                print("c = ", c%3)
                if val == ".":
                    continue

                if val in rows[r]:
                    print("row failed", rows[r])
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    print("column failed")
                    return False
                cols[c].add(val)

                boxValue = r // 3 * 3 + c // 3
                if val in boxs[boxValue]:
                    print("box failed", boxs[boxValue])
                    return False    
                boxs[boxValue].add(val)

        return True
