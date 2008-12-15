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
genome.append([(0,200,0),175,[(0,0),(100,200),(200,100)]])
image = fitness.draw_genome(genome)
image.save('color_poly_test.png','PNG')

# Poly3
fitness.phenotype = 'Poly3'
genome = []
genome.append([(155,0,0),200,[(100,100),(200,300),(100,300),(300,100),(300,200)]])
genome.append([(255,255,0),200,[(0,400),(300,300)]])
genome.append([(0,0,70),100,[(200,300),(300,100),(400,200),(300,300)]])
genome.append([(255,0,255),200,[(200,200)]])
genome.append([(0,200,0),175,[(0,0),(100,200),(200,100)]])
image = fitness.draw_genome(genome)
image.save('color_poly3_test.png','PNG')

# Circle
fitness.phenotype = 'Circ'
genome = []
genome.append([(255,0,0),255,(200,200,150)])
genome.append([(0,255,0),200,(200,100,100)])
genome.append([(0,0,255),150,(200,200,100)])
image = fitness.draw_genome(genome)
image.save('color_circ_test.png','PNG')

# Ellipse
fitness.phenotype = 'Ellip'
genome = []
genome.append([(255,0,0),255,((0,100),(400,300))])
genome.append([(0,255,0),200,((100,0),(200,200))])
genome.append([(0,0,255),150,((100,0),(400,200))])
image = fitness.draw_genome(genome)
image.save('color_ellip_test.png','PNG')

# Rectangle
fitness.phenotype = 'Rect'
genome = []
genome.append([(255,0,0),255,((0,100),(400,300))])
genome.append([(0,255,0),200,((100,0),(200,200))])
genome.append([(0,0,255),150,((150,0),(400,200))])
image = fitness.draw_genome(genome)
image.save('color_rect_test.png','PNG')

# Line
fitness.phenotype = 'Line'
genome = []
genome.append([(255,255,0),200,[(100,100),(100,300),(200,100),(200,300),(300,100),(300,300)]])
genome.append([(0,0,255),150,[(100,100),(300,100),(100,200),(300,200),(100,300),(300,300)]])
image = fitness.draw_genome(genome)
image.save('color_line_test.png','PNG')

# Wide Line
fitness.phenotype = 'WLine'
genome = []
genome.append([(255,255,0),200,[10,(100,100),(100,300),(200,100),(200,300),(300,100),(300,300)]])
genome.append([(0,0,255),150,[5,(100,100),(300,100),(100,200),(300,200),(100,300),(300,300)]])
image = fitness.draw_genome(genome)
image.save('color_wline_test.png','PNG')

###########################################
# Test Grayscale Mode
fitness.color_mode = 'L'
fitness.background_color = 0
# Polygon
fitness.phenotype = 'Poly'
genome = []
genome.append([150,200,[(100,100),(200,300),(100,300),(300,100),(300,200)]])
genome.append([70,150,[(200,300),(300,100),(400,200),(300,300)]])
genome.append([200,175,[(0,0),(100,200),(200,100)]])
image = fitness.draw_genome(genome)
image.save('gray_poly_test.png','PNG')

# Poly3
fitness.phenotype = 'Poly3'
genome = []
genome.append([155,200,[(100,100),(200,300),(100,300),(300,100),(300,200)]])
genome.append([200,200,[(0,400),(300,300)]])
genome.append([70,100,[(200,300),(300,100),(400,200),(300,300)]])
genome.append([255,200,[(200,200)]])
genome.append([200,175,[(0,0),(100,200),(200,100)]])
image = fitness.draw_genome(genome)
image.save('gray_poly3_test.png','PNG')

# Circle
fitness.phenotype = 'Circ'
genome = []
genome.append([200,255,(200,200,150)])
genome.append([150,200,(200,100,100)])
genome.append([100,150,(200,200,100)])
image = fitness.draw_genome(genome)
image.save('gray_circ_test.png','PNG')

# Ellipse
fitness.phenotype = 'Ellip'
genome = []
genome.append([150,255,((0,100),(400,300))])
genome.append([200,200,((100,0),(200,200))])
genome.append([255,150,((100,0),(400,200))])
image = fitness.draw_genome(genome)
image.save('gray_ellip_test.png','PNG')

# Rectangle
fitness.phenotype = 'Rect'
genome = []
genome.append([150,255,((0,100),(400,300))])
genome.append([200,200,((100,0),(200,200))])
genome.append([255,150,((150,0),(400,200))])
image = fitness.draw_genome(genome)
image.save('gray_rect_test.png','PNG')

# Line
fitness.phenotype = 'Line'
genome = []
genome.append([150,200,[(100,100),(100,300),(200,100),(200,300),(300,100),(300,300)]])
genome.append([255,150,[(100,100),(300,100),(100,200),(300,200),(100,300),(300,300)]])
image = fitness.draw_genome(genome)
image.save('gray_line_test.png','PNG')

# Wide Line
fitness.phenotype = 'WLine'
genome = []
genome.append([150,200,[10,(100,100),(100,300),(200,100),(200,300),(300,100),(300,300)]])
genome.append([255,150,[5,(100,100),(300,100),(100,200),(300,200),(100,300),(300,300)]])
image = fitness.draw_genome(genome)
image.save('gray_wline_test.png','PNG')
