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
  i = randint(0, len(data - 1))
  
  if k > 0:
    centroids.append(data[i])

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

#partitions the data into the sets closest to each centroid

def fit(data, centroids):
  pass

#returns k centroids which partition the data optimally into k clusters

def cluster(data, k):
  centroids = find_initial_centroids(data, k)
  
