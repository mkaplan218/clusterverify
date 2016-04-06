from display import display_matrix
from parse import parse
from parse import parse_raw
from kmeans import cluster

def test_display_matrix():
  z_test = [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
  display_matrix(z_test, title = "Test - Z")

def test_display_data():
  real_data_test = parse_raw("1 o 2 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 1 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 1 1 1 0 0 0 1 1 1 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", 16, 8)[0]

  display_matrix(real_data_test, title = "First real character")

#Takes a list of integers representing pixel locations in a 5x5 grid
def generate_datapoint(L):
  p = [0]*25
  for i in range(25):
    if i in L:
      p[i] = 1
  return p

def test_cluster_5x5():
  z1 = [0,1,2,3,4,8,12,16,20,21,22,23,24]
  z2 = [1,2,3,4,8,9,12,13,16,17,21,22,23,24]
  z3 = [0,1,2,3,7,11,15,16,17,18]
  c1 = [1,2,3,6,8,11,16,18,21,22,23]
  c2 = [6,7,8,11,16,17,18]
  c3 = [1,2,3,6,11,16,17,18]
  o1 = [6,7,8,11,13,16,17,18]
  o2 = [1,2,3,6,8,11,13,16,18,21,22,23]
  o3 = [6,7,8,9,11,14,16,17,18,19]
  e1 = [1,2,3,6,11,12,13,16,21,22,23]
  e2 = [1,2,6,11,12,16,21,22]
  e3 = [1,2,3,6,11,12,16,21,22,23]

  letters = [z1, z2, z3, c1, c2, c3, o1, o2, o3, e1, e2, e3]
  datapoints = [generate_datapoint(x) for x in letters]

  centroids = cluster(datapoints, 4)
  
  for c in centroids:
    display_matrix(parse(c, 5, 5))
  

def test_all():
  test_display_matrix()
  test_display_data()
  test_cluster_5x5()
