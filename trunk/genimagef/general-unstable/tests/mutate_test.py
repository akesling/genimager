#!/usr/bin/python
# Mutate Test Script
# Goes through the mutate functions and tests them
import random
random.seed()
import sys
sys.path.append('..')
import mutate
mutate.imagewidth = 20
mutate.imageheight = 20
mutate.phenotype = "Poly"
for color_mode in ['RGB','L']:
   mutate.color_mode = color_mode
   mDNA = []
   for i in xrange(500): mutate.insert_chromosome(mDNA)
   for i in xrange(300): mutate.remove_chromosome(mDNA)
   for i in xrange(10000): mutate.switch_chromosomes(mDNA)
   for i in xrange(10000): mutate.shuffle_chromosomes(mDNA)
   for i in xrange(10000): mutate.increment_chromosome(mDNA)
   for i in xrange(10000): mutate.decrement_chromosome(mDNA)
   for i in xrange(100000): mutate.mutate_point(mDNA) # hopefully tests each func in here
   for i in xrange(10000): mutate.new_color(mDNA)
   for i in xrange(10000): mutate.change_color(mDNA)
   for i in xrange(10000): mutate.switch_colors(mDNA)
   for i in xrange(10000): mutate.new_opacity(mDNA)
   for i in xrange(10000): mutate.change_opacity(mDNA)
   for i in xrange(10000): mutate.switch_opacities(mDNA)
print "Pass!"
