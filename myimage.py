#!/usr/bin/env python

import numpy, ctypes

class MyImage:
  def __init__(self):
    self.lib = ctypes.cdll.LoadLibrary('./myimg.so')
    self.nrows = self.lib.image_nrows()
    self.ncols = self.lib.image_ncols()
    self.data = numpy.empty((self.nrows,self.ncols), dtype=numpy.double)
  def get(self):
    self.lib.image_get(ctypes.c_void_p(self.data.ctypes.data))

if __name__ == '__main__':
  img = MyImage()
  print(img.nrows,img.ncols)
  print(img.data)
  img.get()
  print(img.data)
