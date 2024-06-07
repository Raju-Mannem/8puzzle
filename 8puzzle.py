# 8 puzzle in python 
import heapq

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.moves = []

    def __lt__(self, other):
        return False

    def get_blank_pos(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return (row, col)

    def get_moves(self):
        moves = []
        row, col = self.get_blank_pos()

        if col > 0:
            left = Puzzle([r[:] for r in self.board])
            left.board[row][col], left.board[row][col-1] = left.board[row][col-1], left.board[row][col]
            left.moves.append('L')
            moves.append(left)

        if col < 2:
            right = Puzzle([r[:] for r in self.board])
            right.board[row][col], right.board[row][col+1] = right.board[row][col+1], right.board[row][col]
            right.moves.append('R')
            moves.append(right)

        if row > 0:
            up = Puzzle([r[:] for r in self.board])
            up.board[row][col], up.board[row-1][col] = up.board[row-1][col], up.board[row][col]
            up.moves.append('U')
            moves.append(up)

        if row < 2:
            down = Puzzle([r[:] for r in self.board])
            down.board[row][col], down.board[row+1][col] = down.board[row+1][col], down.board[row][col]
            down.moves.append('D')
            moves.append(down)

        return moves

    def is_solved(self):
        return self.board == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def solve(start):
    heap = []
    visited = set()
    heapq.heappush(heap, (0, start))

    while heap:
        _, puzzle = heapq.heappop(heap)

        if puzzle.is_solved():
            return puzzle.moves

        for move in puzzle.get_moves():
            if tuple(map(tuple, move.board)) not in visited:
                visited.add(tuple(map(tuple, move.board)))
                cost = len(move.moves) + heuristic(move)
                heapq.heappush(heap, (cost, move))

    return None

def heuristic(puzzle):
    dist = 0

    for row in range(3):
        for col in range(3):
            val = puzzle.board[row][col]
            if val != 0:
                target_row = (val - 1) // 3
                target_col = (val - 1) % 3
                dist += abs(row - target_row) + abs(col - target_col)

    return dist

# Example usage
start = Puzzle([[1, 0, 2], [3, 4, 5], [6, 7, 8]])
moves = solve(start)

if moves:
    print("Solved in", len(moves), "moves:", moves)
else:
    print("Unsolvable puzzle!")

# In the above code, the Puzzle class represents a single state of the puzzle, with the board as a 2D array and the moves list keeping track of the sequence of moves taken to reach that state. The get_blank_pos method returns the row and column of the blank tile (represented by the value 0), the get_moves method generates all possible moves from the current state

