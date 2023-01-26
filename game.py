def create_grid(rows, cols):
    grid = [[0 for i in range(cols)] for j in range(rows)]
    return grid

def apply_rules(grid, row, col):
    num_neighbors = 0

    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if not (i == row and j == col):
                    if grid[i][j] == 1:
                        num_neighbors += 1

    if grid[row][col] == 1:
        if num_neighbors < 2 or num_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if num_neighbors == 3:
            return 1
        else:
            return 0

def next_generation(grid):
    new_grid = create_grid(len(grid), len(grid[0]))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = apply_rules(grid, i, j)

    return new_grid

def continue_generations(grid, num_generations):
    for i in range(num_generations):
        grid = next_generation(grid)
        print("Generation", i+1)
        print_grid(grid)
    return grid

def print_grid(grid):
    print("+" + "-" * (len(grid[0]) * 2 + 1) + "+")
    for i in range(len(grid)):
        print("|", end="")
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                print("0 |", end="")
            else:
                print("  |", end="")
        print("|")
        print("+" + "-" * (len(grid[0]) * 2 + 1) + "+")

rows = int(input("Enter the number of rows in the grid: "))
cols = int(input("Enter the number of columns in the grid: "))

grid = create_grid(rows, cols)

print("Enter the coordinates of each cell that should be populated, separated by a space.")
print("For example, to populate the cell at row 2 and column 3, enter '2 3'.")
print("Enter 'done' when you are finished entering coordinates.")

while True:
    coordinates = input("Enter coordinates: ")
    if coordinates == "done":
        break
    else:
        coordinates = coordinates.split(" ")
        row = int(coordinates[0])
        col = int(coordinates[1])
        if row < 0 or row >= rows or col < 0 or col >= cols:
            print("Error: coordinates are out of bounds. Please try again.")
        else:
            grid[row][col] = 1

print("Initial state of the grid:")
print_grid(grid)

grid = next_generation(grid)

print("Next generation of the grid:")
print_grid(grid)

num_generations = int(input("Enter the number of generations to continue: "))
final_grid = continue_generations(grid, num_generations)

print("Final state of the grid:")
print_grid(final_grid)