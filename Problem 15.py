size = 20
grid = [[0 for j in range(size)] for i in range(size)]
total = 1
        
for i in range(size-1,0-1,-1):
    for j in range(size):
        if (i == size-1 or j == 0):
            grid[i][j] = 1
        else:
            grid[i][j] = grid[i+1][j] + grid[i][j-1]
        total += grid[i][j]

print(total)
