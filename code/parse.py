def parse(data, rows, cols):
  assert(len(data) == rows*cols)

  M = []
  for row in xrange(rows):
    new_row = []
    for col in xrange(cols):
      new_row.append(int(data[row*cols + col]))
    M.append(new_row)

  return M
  

#Parse a matrix out of a line of input from our data
def parse_raw(input, rows, cols):
  raw = input.split(" ")

  id = raw[0]
  letter = raw[1]
  next_id = raw[2]
  word_id = raw[3]
  position = raw[4]
  fold = raw[5]
  raw_data = raw[6:]

  return (parse(raw_data, rows, cols), id, letter, next_id, word_id, position, fold)
