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
