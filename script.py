import copy
import time

class Sudoku:

  def __init__(self, board):
    self.board = board
    self.__printMat(self.board)
    print ()
    self.board_deep_copy = copy.deepcopy(self.board)

    starttime = time.clock()
    self.solve()
    endtime = time.clock()

    if (self.board_deep_copy == self.board):
      print ('There is error in the question')
    else:
      self.__printMat(self.board)

    print (f'The code took {endtime - starttime:0.2f}s')

  def solve(self):
    try:
      self.main()
    except RuntimeError:
      return False

    if self.isComplete():
      return True

    i, j = 0, 0
    for rowidx, row in enumerate(self.board):
      for colidx, col in enumerate(row):
        if col == ".":
          i, j = rowidx, colidx

    possibility = self.get_all_Possibilities(i, j)
    snapshot = copy.deepcopy(self.board)

    for value in possibility:
      self.board[i][j] = value
      result = self.solve()

      if result == True:
        return True
      else:
        self.board = copy.deepcopy(snapshot)
    return False

  #checks if the board is full.
  def isComplete(self):
    for i in range(0, 9):
      for j in range(0, 9):
        if self.board[i][j] == ".":
          return False

    return True

  #This is the main function.
  def main(self):

    something_changed = False

    #loop through all field of board.
    for i in range(0, 9):
      for j in range(0, 9):
        #Get all possibilities of current board element.
        possibilities = self.get_all_Possibilities(i, j)

        #If no any possibility is met or if the element is not dot then again loop over.
        if possibilities == False:
          continue

        if len(possibilities) == 0:
          raise RuntimeError('No moves left')

        #if only one possibility is returned then insert it into board.
        if len(possibilities) == 1:
          self.board[i][j] = possibilities[0]
          something_changed = True

    if something_changed == False:
      return

  #Get Possibilities.
  def get_all_Possibilities(self, i, j):

    if self.board[i][j] != '.':
      return False

    possibility = {str(i) for i in range(1, 10)}
    
    #check row.
    for row in self.board[i]:
      possibility -= set(row)

    #check column.
    for row in range(0, 9):
      possibility -= set(self.board[row][j])

    #check possibility in nine squares.
    iStart = (i // 3) * 3
    jStart = (j // 3) * 3

    subboard = self.board[iStart: iStart + 3]
    for rowIdx, row in enumerate(subboard):
      subboard[rowIdx] = row[jStart: jStart + 3]

    for row in subboard:
      for col in subboard:
        possibility -= set(col)

    return list(possibility)

  def __printMat(self, matrix):

    for row in range(0, 9):
      for col in range(0, 9):
        print (matrix[row][col] + ' ', end = ' ')
      print ()

  def return_result(self):
    return self.board

if __name__ == "__main__":
  data = [
      ["2", "8", ".", "1", "3", ".", "7", ".", "9"],
      ["7", "4", "5", "2", ".", "9", "8", "1", "3"],
      ["3", ".", "1", "5", "8", "7", "2", "4", "6"],
      ["1", "2", ".", ".", ".", "8", ".", "3", "7"],
      [".", ".", ".", "7", "4", "3", "5", ".", "1"],
      [".", "7", "3", ".", "2", "1", "4", "6", "8"],
      ["9", "3", "2", "8", "1", "5", ".", "7", "4"],
      [".", "1", "7", "4", "9", "2", "3", "8", "5"],
      ["4", "5", ".", ".", "7", "6", "1", ".", "2"],
  ]
  sudoku = Sudoku(data)
