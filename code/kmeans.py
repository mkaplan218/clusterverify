from random import randint
from copy import deepcopy

from parse import parse

#In this file, I am assuming that the 6 metadata entries at the front of each
#  raw data point hae been stripped off during initial parsing.

#returns the distance between two data points

def distance(X, Y):
  assert(len(X) == len(Y))

  d = 0
  for pixel in range(len(X)):
    if X[pixel] != Y[pixel]:
      d += 1
  return d

#Intelligently find some starting centroids, instead of choosing k random points.
#  Choose one random point to start with, then find the point with largest
#  sum of distances from all other centroids selected so far and make it a centroid
#  until k have been chosen.

def find_initial_centroids(data, k):
  assert(len(data) >= k)
  data = deepcopy(data)

  centroids = []
  initial = randint(0, len(data - 1))
  
  if k > 0:
    centroids.append(data[initial])

  while (len(centroids) < k):
    new_i = None
    max_distance = None
    for i in range(len(data)):
      total_distance = 0
      for c in centroids:
        total_distance += distance(data[i], c)
      if (new_i == None) or (total_distance > max_distance):
        new_i = i
        max_distance = total_distance
    centroids.append(data.pop(i))
    
  return centroids

#Finds the representative centroid of a subset of data, based on the most
#  common pixel in each position

def find_centroid(data):
  assert(len(data) > 0)

  centroid = [0]*len(data[0])
  for i in range(len(centroid)):
    sum = 0
    for point in data:
      sum += point[i] #Assuming pixel values are either 1 or 0
    if (sum / len(data)) >= .5: #If a majority of pixels have value 1
      centroid[i] = 1

  return centroid

#Compares two sets of points for equality

def centroids_equal(old, new):
  assert((len(old) > 0) and (len(old) == len(new)))
  assert(len(old[0]) == len(new[0]))

  for i in len(old):
    for j in len(old[i]):
      if (old[i][j] != new[i][j]):
        return False

  return True
    

#partitions the data into the sets closest to each centroid

def fit(data, centroids):
  k = len(centroids)

  #Maps the index of a centroid to the set of points closest to it
  clusters = {x: [] for x in range(k)}

  for point in data:
    min_d = None
    best = None
    for i in range(k):
      d = distance(point, centroids[i])
      if ((min_d == None) or (d < min_d)):
        min_d = d
        best = i
    clusters[best].append(point)

  return clusters

#returns k centroids which partition the data optimally into k clusters

def cluster(data, k):
  old_centroids = find_initial_centroids(data, k)
  while True: #scary, whatever yolo
    clusters = fit(data, old_centroids)
    new_centroids = [find_centroid(clusters[x]) for x in range(len(clusters))]
    if centroids_equal(old_centroids, new_centroids):
      break
       
  return new_centroids


