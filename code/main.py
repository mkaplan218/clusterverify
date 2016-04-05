# LOL
# TERM PROJECT 701
# mfkaplan and jfarrus
import argparse
import numpy as np

# runs main
if __name__ == '__main__':
  parser = init_parser()
  args = parser.parse_args()
  main(args)

######################
# FILE AND HUMAN IO
######################
def main(args):
  return 0

def init_parser():
  parser = argparse.ArgumentParser(description = 'Some Clustering stuff')
  parser.add_argument('filepath', required = True, help = 'Data file for clustering')
  parser.add_argument('-m', required = False, default = 'kmeans',
      help = 'Method of clustering (default is KMeans)')
  return parser

#######################
# PUT KMEANS BELOW HERE
#######################


# poop
