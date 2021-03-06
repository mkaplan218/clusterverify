# LOL
# TERM PROJECT 701
# mfkaplan and jfarrus
import argparse
import numpy as np
from display import display_char
from sklearn import mixture

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

  subset = data #[data[x] for x in xrange(0, n) if labels[x] in 'abc']
  print 'labels: ', len(labels)

  counts = {}
  for elem in labels:
    if elem not in counts:
      counts[elem] = 1
    else:
      counts[elem] += 1
  print counts
  print 'subset: ', len(subset)

  clusters = cluster(subset, args.m, args.k)

  write_clusters(clusters, args.o)

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
  parser.add_argument('-o', default = 'out.data',
      help = 'Output file for clustered labels')
  return parser

def write_clusters(clusters, outfile):
  output = open(outfile, 'w')
  for elem in clusters:
    output.write(str(elem))
    output.write('\n')
  return 0

def cluster(data, method, k):
  print 'clustering with method: ', method, ' and k: ', k
  clusters = []

  human_needed = True
  while human_needed:
    if method == 'kmeans':
      duplicates = False
      unique_labels = []
      # TODO: move all of this out into a separate function
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
          if label not in unique_labels:
            unique_labels.append(label)
          else:
            k -= 1
            duplicates = True
          # unhashable type...
          #human[cent] = label

          # TODO
          # how to check for duplicates?

      # 3. ask if there needs to be more clusters
      if not duplicates:
        more = raw_input('Is ' + str(k) + ' enough clusters? (yes/no): ')
        if more == 'no':
          k += 1
        else:
          human_needed = False
          clusters = kmeans.fit(data, centroids)
      else:
        print 'Removing duplicate clusters'

    elif method == 'gmm':
      # GMM stuff
      print 'gmm incoming!'

    else:
      # who knows what will go here? long-term goals
      print method, ' is not a valid method right now. sorry!'


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

