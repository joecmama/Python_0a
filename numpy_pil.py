#!/usr/bin/env python

# NEED: "module unload python" then "module load anaconda"

from PIL import Image
import numpy
from matplotlib.pyplot import *

# Read a TIFF file (from http://www-eng-x.llnl.gov/documents/tests/tiff.html)
im = Image.open('a_image.tif')

# Convert to numpy array
a = numpy.array(im)
print('a:')
print(a.shape)
print(a)

# Take 2D FFT
b = numpy.fft.fft2(a)
print('b:')
print(b.shape)
print(b)

# Random array of same shape
r = numpy.random.rand(*b.shape)
print('r:')
print(r.shape)
print(r)

# Matrix multiply
rb = numpy.dot(r.T,b)
print('rb:')
print(rb.shape)
print(rb)

# Inverse 2D FFT
c = numpy.fft.ifft2(rb)
print('c:')
print(c.shape)
print(c)

# FFT shift (move zero-frequency component to center of spectrum)
d = numpy.fft.fftshift(c)
print('d:')
print(d.shape)
print(d)

# get magnitudes
dmag = numpy.absolute(d)
print('dmag:')
print(dmag.shape)
print(dmag)

# maximum element
m = dmag.max()
print('m:')
print(m)

# array indices of maximum element
mij = numpy.unravel_index(dmag.argmax(), d.shape)
print('mij:')
print(mij)

# display as grayscale
Image.fromarray(dmag, 'L').show()

# display as RGB
Image.fromarray(dmag, 'RGB').show()

# get a submatrix
submat = dmag[2:6, 3:7]

# write it to a text file
numpy.savetxt('submat.txt', submat)

# get a row
drow = dmag[10]
print('drow:')
print(drow)

# plot values in red, square roots in blue
xvals = range(0,len(drow))
print('xvals:')
print(xvals)

plot(xvals, drow, 'r', xvals, numpy.sqrt(drow), 'b')
show()
