class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            my_set = set()
            for col in range(9):
                item = board[row][col]
                if item in my_set:
                    return False
                elif item != ".":
                    my_set.add(item)
        
        for row in range(9):
            my_set = set()
            for col in range(9):
                item = board[col][row]
                if item in my_set:
                    return False
                elif item != ".":
                    my_set.add(item)
        
        start_pos = [(0,0),(0,3),(0,6),
                     (3,0),(3,3),(3,6),
                     (6,0),(6,3),(6,6)]
        
        for r, c in start_pos:
            my_set = set()
            for row in range(r, r+3):
                for col in range(c, c+3):
                    item = board[row][col]
                    if item in my_set:
                        return False
                    elif item != ".":
                        my_set.add(item)
        return True