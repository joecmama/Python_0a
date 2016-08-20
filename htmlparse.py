#!/usr/bin/env python

from HTMLParser import HTMLParser
from urllib2 import urlopen

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a': # HTML link
            attrs = dict(attrs)
            print(attrs)
            print(attrs['href'])

u = urlopen('http://www.rochester.edu').read()
#print(u)
MyHTMLParser().feed(u)

