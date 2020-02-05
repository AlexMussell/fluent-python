## tuples support all methods lists do, except: adding items, removing items, and tuple.reversed. 
# However, reversed(tuple) works.

# Slicing - all sequence types support
# seq[start:stop:step] - can step negative

## Mutlidimensional slicing and ellipsis
# format - a[m:n, k:l]

# ... is a shortcut for multidimentional arrays. Eg a 4d array is arr[i, ...] == arr[i, :, :, :,]


## Building list of lists

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'

# Same as:
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)    # New row is added 3x to board


# However, this may seem correct, however you create 3 references to the same object
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'X'
# [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]

# Same as:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)    # Same row is appended 3x to board
