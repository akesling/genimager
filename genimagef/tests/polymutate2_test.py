#!/usr/bin/python
# polymutate2_test.py
# test script for new mutate library
import sys
sys.path.append('..')
import polymutate2 as mutate
genome = []
mutate.imageheight = 100
mutate.imagewidth = 100
mutate.color_mode = 'RGB'
for i in xrange(int(1E6)):
   genome = mutate.mutate(genome)
mutate.color_mode = 'L'
for i in xrange(int(1E6)):
   genome = mutate.mutate(genome)
