#!/usr/bin/python
# Mutate Test Script
# Goes through the mutate functions and tests them
ImageWidth = 20
ImageHeight = 20
import random
random.seed()
import mutate
mDNA = []
for i in xrange(500): mutate.insert_chromosome(mDNA)
for i in xrange(300): mutate.remove_chromosome(mDNA)
for i in xrange(10000): mutate.switch_chromosomes(mDNA)
for i in xrange(10000): mutate.shuffle_chromosomes(mDNA)
for i in xrange(10000): mutate.increment_chromosome(mDNA)
for i in xrange(10000): mutate.decrement_chromosome(mDNA)
for i in xrange(10000): mutate.insert_point(mDNA)
for i in xrange(5000): mutate.remove_point(mDNA)
for i in xrange(10000): mutate.switch_points(mDNA)
for i in xrange(10000): mutate.shuffle_points(mDNA)
for i in xrange(10000): mutate.move_point(mDNA)
for i in xrange(10000): mutate.shift_point(mDNA)
for i in xrange(10000): mutate.increment_point(mDNA)
for i in xrange(10000): mutate.decrement_point(mDNA)
for i in xrange(10000): mutate.new_color(mDNA)
for i in xrange(10000): mutate.change_color(mDNA)
for i in xrange(10000): mutate.switch_colors(mDNA)
for i in xrange(10000): mutate.new_opacity(mDNA)
for i in xrange(10000): mutate.change_opacity(mDNA)
for i in xrange(10000): mutate.switch_opacities(mDNA)
