# LOL
# TERM PROJECT 701
# mfkaplan and jfarrus
import argparse
import numpy as np
from display import display_char
import kmeans

# current centroids
centroids = []
# all points that a human has labeled
human_points = []
# labels for the points a human has touched (ordered with above)
human_labels = []
human = {}

######################
# FILE AND HUMAN IO
######################
def main(args):
  raw_data = np.loadtxt(args.file, dtype = np.str)
  data = raw_data[ : , 6: ].astype(np.float).tolist()
  labels = raw_data[ : , 1].tolist()

  n = len(labels)

  subset = [data[x] for x in xrange(0, n) if labels[x] == 'c' or labels[x] == 'x']
  print 'labels: ', len(labels)

  counts = {}
  for elem in labels:
    if elem not in counts:
      counts[elem] = 0
    else:
      counts[elem] += 1
  print counts
  print 'subset: ', len(subset)

  clusters = cluster(subset, args.m, args.k)

  # nothing else went wrong
  print 'Exiting nicely!'
  return 0

def init_parser():
  parser = argparse.ArgumentParser(description = 'Some Clustering stuff')
  parser.add_argument('file', help = 'Data file path for clustering')
  parser.add_argument('-m', default = 'kmeans',
      help = 'Method of clustering (default is KMeans)')
  parser.add_argument('-k', default = '2', type = int,
      help = 'Initial number of clusters (default is 2)')
  return parser

def cluster(data, method, k):
  print 'clustering with method: ', method, ' and k: ', k
  clusters = []

  human_needed = True
  while human_needed:
    if method == 'kmeans':
      # 1. cluster with kmeans
      centroids = kmeans.cluster(data, k)

      # 2. ask for human to label clusters
      for cent in centroids:
        if cent not in human_points:
          # display centroid
          display_char(cent, 16, 8, 'Centroid')

          # ask for label from h00man
          label = raw_input('Please label this centroid: ')

          # save point with label to labeled_points
          human_points.append(cent)
          human_labels.append(label)
          # unhashable type...
          #human[cent] = label

          # TODO
          # how to check for duplicates?

      # 3. ask if there needs to be more clusters
      more = raw_input('Is this enough clusters? (yes/no): ')
      if more == 'no':
        k += 1
      else:
        human_needed = False
        clusters = kmeans.fit(data, centroids)

    else:
      # who knows what will go here? long-term goals
      print method.m, ' is not a valid method right now. sorry!'


  return clusters

#######################
# PUT KMEANS BELOW HERE
#######################

# handle labeling in this file, just keep track of labeled points in an nparray, and use the fit() function to label clusters

# poop


# runs main
if __name__ == '__main__':
  parser = init_parser()
  args = parser.parse_args()
  main(args)

