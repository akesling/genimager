#!/usr/bin/python
# Fitness Test Script
# Goes through the fitness functions and tests them
# The majority of this test is testing drawing from the genome
import sys
sys.path = sys.path + ['..']
import fitness
fitness.imagewidth = 400
fitness.imageheight = 400

# Test Color 'RGB' First
fitness.color_mode = 'RGB'
fitness.background_color = (0,0,0)
# Polygon
fitness.phenotype = 'Poly'
genome = []
genome.append([(150,0,0),200,[(100,100),(200,300),(100,300),(300,100),(300,200)]])
genome.append([(0,0,70),150,[(200,300),(300,100),(400,200),(300,300)]])
genome.append([(0,200,0),70,[(0,0),(100,200),(200,100)]])
image = fitness.draw_genome(genome)
image.save('color_poly_test.png','PNG')

# Poly3
fitness.phenotype = 'Poly3'
genome = []
genome.append([(155,0,0),200,[(100,100),(200,300),(100,300),(300,100),(300,200)]])
genome.append([(255,255,0),200,[(0,400),(300,300)]])
genome.append([(0,0,70),100,[(200,300),(300,100),(400,200),(300,300)]])
genome.append([(255,0,255),200,[(200,200)]])
genome.append([(0,255,0),200,[(0,0),(100,200),(200,100)]])
image = fitness.draw_genome(genome)
image.save('color_poly3_test.png','PNG')


# Test Grayscale Second
fitness.color_mode = 'L'
fitness.background_color = 0
