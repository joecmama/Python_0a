#!/usr/bin/env python

# matplotlib

from matplotlib.pyplot import *
from math import pi,sin

xvals = [2*pi*x/100 for x in range(0,101)]
yvals = [sin(x) for x in xvals]
plot(xvals, yvals)
xlim([0,2*pi])
ylim([-1,1])
xlabel('x')
ylabel('sin x')
show()
