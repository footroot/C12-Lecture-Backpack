# def minesweeper(grid):
#     for row in grid:
#         for col in row:
#             print(col, end=" ")
#         print()

def minesweeper(grid):

    new_grid = [[None for c in r] for r in grid]

    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            
            if grid[row_index][col_index] == "#":
                new_grid[row_index][col_index] = "#"
                continue

            total_mines = 0

            if col_index-1 >= 0 and grid[row_index][col_index-1] == "#":
                total_mines += 1

            if row_index+1 < len(grid) and grid[row_index+1][col_index] == "#":
                total_mines += 1

            if col_index-1 >= 0 and row_index+1 < len(grid) and grid[row_index+1][col_index-1] == "#":
                total_mines += 1

            if col_index+1 < len(grid[row_index]) and row_index+1 < len(grid) and grid[row_index+1][col_index+1] == "#":
                total_mines += 1
            
            if col_index+1 < len(grid[row_index]) and grid[row_index][col_index+1] == "#":
                total_mines += 1

            if col_index-1 >= 0 and row_index-1 >= 0 and grid[row_index-1][col_index-1] == "#":
                total_mines += 1

            if row_index-1 >= 0 and grid[row_index-1][col_index] == "#":
                total_mines += 1

            if col_index+1 < len(grid[row_index]) and row_index-1 >= 0 and grid[row_index-1][col_index+1] == "#":
                total_mines += 1

            new_grid[row_index][col_index] = total_mines

    return new_grid

# grid = [
#     ['#', '0', '0', '0', '0'], # [(0,0), (0,1), (0,2), (0,3), (0,4)]
#     ['0', '0', '0', '#', '0'], # [(1,0), (1,1), (1,2), (1,3), (1,4)]
#     ['0', '#', '0', '#', '0'], # [(2,0), (2,1), (2,2), (2,3), (2,4)]
#     ['0', '0', '#', '0', '#'],
#     ['#', '0', '0', '0', '0']
# ]
# for row in minesweeper(grid):
#     for col in row:
#         print(col, end=" ")
#     print()


def minesweeper(grid):

    new_grid = [[None for c in r] for r in grid]

    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            
            if grid[row_index][col_index] == "#":
                new_grid[row_index][col_index] = "#"
                continue

            total_mines = 0

            for r in range(row_index-1, row_index+2):
                for c in range(col_index-1, col_index+2):
                    if 0 <= r < len(grid) and 0 <= c < len(grid[row_index]) and grid[r][c] == "#":
                        total_mines += 1
            
            new_grid[row_index][col_index] = total_mines
    
    return new_grid

grid = [
    ['#', '0', '0', '0', '0'], # [(0,0), (0,1), (0,2), (0,3), (0,4)]
    ['0', '0', '0', '#', '0'], # [(1,0), (1,1), (1,2), (1,3), (1,4)]
    ['0', '#', '0', '#', '0'], # [(2,0), (2,1), (2,2), (2,3), (2,4)]
    ['0', '0', '#', '0', '#'],
    ['#', '0', '0', '0', '0']
]
for row in minesweeper(grid):
    for col in row:
        print(col, end=" ")
    print()