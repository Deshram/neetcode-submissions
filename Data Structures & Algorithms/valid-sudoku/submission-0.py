class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(0,9)]
        cols = [set() for _ in range(0,9)]
        boxes = {}

        for r in range(0,9):
            for c in range(0,9):
                val = board[r][c]
                
                if val == ".":
                    continue

                box_idx = (r//3, c//3)
                box = boxes.get(box_idx, set())

                if val in rows[r] or val in cols[c] or val in box:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                box.add(val)

                boxes[box_idx] = box

        return True