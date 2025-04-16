class Solution:
	def isValidSudoku(self, board):
		outcome = True
		posDict = {}
		gridDict = {}
		outBreak = False
		for y in range(9):
			for x in range(9):
				if(board[y][x] != "."):
					if(not board[y][x] in posDict):
						posDict[board[y][x]] = [[y, x]]
						gridDict[board[y][x]] = [[y//3, x//3]]
					else:
						for arr in posDict[board[y][x]]:
							if(arr[0] == y):
								outcome = False
							elif(arr[1] == x):
								outcome = False
						for arr in gridDict[board[y][x]]:
							if(arr == [y//3, x//3]):
								outcome = False
						if(not outcome):
							outBreak = True
							break
						posDict[board[y][x]].append([y, x])
						gridDict[board[y][x]].append([y//3, x//3])
			if(outBreak):
				break
		return outcome


board =\
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))
