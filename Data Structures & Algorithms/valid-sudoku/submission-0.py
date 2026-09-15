class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            nums = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in nums:
                        return False
                    nums.append(board[i][j])

        for j in range(9):
            nums = []
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in nums:
                        return False
                    nums.append(board[i][j])

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            if board[i][j] in nums:
                                return False
                            nums.append(board[i][j])

        return True