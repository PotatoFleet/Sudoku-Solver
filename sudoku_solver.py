# function to check if a number target in position pos is valid
# a position is valid if the number target is not found in the same row, column or box
def isValid(board, target, pos):

	for i in range(9):

		if (board[pos[0]][i] == target) or (board[i][pos[1]] == target) or (board[pos[0] // 3 * 3 + i // 3][pos[1] // 3 * 3 + i % 3] == target):

			return False

	return True

# main function
# start -> the ith empty spot
# empty_cells -> a list of all the empty cell positions
# board -> the board -_-
def dfs(start, empty_cells, board):

	if start == len(empty_cells):
		return True #solved

	i, j = empty_cells[start]

    # Testing all numbers to fill in empty slot
	for k in range(1, 10):

		k = str(k)

		if not isValid(board, k, (i, j)):
			continue

		board[i][j] = k

		if dfs(start+1, empty_cells, board):
			return True

        # Reverts back to original if doesn't return True
		board[i][j] = '.'

# finding all empty cells and then calling dfs()
def solve(board):

	empty_cells = []

	for i in range(9):

		for j in range(9):

			if board[i][j] == '.':

				empty_cells.append([i, j])

	dfs(0, empty_cells, board)
