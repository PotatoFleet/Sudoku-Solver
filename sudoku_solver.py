def solve(board):

	rows = [set() for _ in range(9)]
	cols = [set() for _ in range(9)]
	blocks = [set() for _ in range(9)]

	empty_cells = []

	for i in range(9):

		for j in range(9):

			if board[i][j] == '.':

				empty_cells.append([i, j])

			else:

				rows[i].add(board[i][j])

				cols[j].add(board[i][j])

				blocks[i // 3 * 3 + j // 3].add(board[i][j])

	def dfs(start):

		if start == len(empty_cells): return True # Done

		i, j = empty_cells[start]

		for num in range(1, 10):

			snum = str(num)
			block = i // 3 * 3 + j // 3

			if snum in rows[i] or snum in cols[j] or snum in blocks[block]:
				continue

			rows[i].add(snum)
			cols[j].add(snum)
			blocks[block].add(snum)
			board[i][j] = snum

			if dfs(start + 1): return True # if possible

			rows[i].remove(snum)
			cols[j].remove(snum)
			blocks[block].remove(snum)
			board[i][j] = '.'

		return False

	dfs(0)
