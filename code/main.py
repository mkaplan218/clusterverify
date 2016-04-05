# LOL
# TERM PROJECT 701
# mfkaplan and jfarrus
import argparse
import numpy as np

######################
# FILE AND HUMAN IO
######################
def main(args):
  # TODO: figure out how to take in
  raw_data = np.loadtxt(args.file, dtype = np.str)
  data = raw_data[ : , 6: ].astype(np.float)
  labels = raw_data[ : , 1]
  print(labels.shape)
  print(data.dtype)
  counts = {}
  for elem in np.unique(labels):
    counts[elem] = 0
  for elem in labels:
    counts[elem] += 1
  print(counts)
  return 'Exiting nicely'

def init_parser():
  parser = argparse.ArgumentParser(description = 'Some Clustering stuff')
  parser.add_argument('file', help = 'Data file path for clustering')
  parser.add_argument('-m', default = 'kmeans',
      help = 'Method of clustering (default is KMeans)')
  return parser

#######################
# PUT KMEANS BELOW HERE
#######################


# poop


# runs main
if __name__ == '__main__':
  parser = init_parser()
  args = parser.parse_args()
  main(args)

