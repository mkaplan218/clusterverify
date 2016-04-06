def to_matrix(data_array, rows, cols):
  M = []
  for row in range(rows):
    new_row = []
    for col in range(cols):
      new_row.append(data_array[row*cols + col])
    M.append(new_row)
  return M

#display a character given as a matrix, M
def display_matrix(M, title = ""):
  if len(title) > 0:
    print("Printing character: " + title + "\n")

  for row in M:
    new_row = ""
    for col in row:
      if col == 1:
        new_row += "@ "
      else:
        new_row += ". "
    print(new_row)
  print
