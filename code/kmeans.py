#returns the distance between two data points
def distance(X, Y):
  d = 0
  for row in range(len(X)):
    for col in range(len(X[row]):
      if X[row][col] != Y[row][col]:
        d += 1
  return d

#partitions the data into the sets closest to each centroid
def fit(data, centroids):
  pass

#returns k centroids which partition the data optimally into k clusters
def cluster(data, k):
  pass

#allows the user to assign character names to each centroid given
def label(centroids):
  pass
