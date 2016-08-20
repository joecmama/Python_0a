#!/usr/bin/env python

# Run this code on CIRC computing node to get 4 node for parallel computing?
# srun -p debug --pty --time=01:00:00 $* bash -l n=4

from time import time

def fractional_part(x): # a slow way to calculate!
  while x > 1:
      x -= 1
  return '%.2f' % x

#print(fractional_part(3.1415))

xlst = [20485734.12, 20161059.34, 20792768.56, 20137589.78]

# serial
start = time()
results = map(fractional_part, xlst)
elapsed = time() - start
print(results)
print('elapsed time: %.3f sec\n' % elapsed)

# parallel
from multiprocessing import Pool
p = Pool(4) # number of processes
start = time()
results = p.map(fractional_part, xlst)
elapsed = time() - start
print(results)
print('elapsed time: %.3f sec\n' % elapsed)
