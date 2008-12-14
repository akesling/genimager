#!/usr/bin/python
#  Mutate Function
#  This mutation function is made up of four basic sections,
#   and each of these four sections has four actions.
#  Every action has an equal weight except for special
#   cases (where noted).
#
#  The base mutate() function deepcopies the genome argument
#   it's handed and eventually returns a mutated genome.
#  Every other function modifies the new (mutated) genome in place.
#
#  Special Case: If the genome has no chomosomes, 
#   then it forces the mutation 'Insert Chomosome'.
import copy
from genetic_imager import random
global imagewidth, imageheight, color_mode, phenotype

def mutate(genome):
   """
   Mutate Function
   This mutation function is made up of four basic sections,
    and each of these four sections has four actions.
   Every action has an equal weight except for special
    cases (where noted).

   The base mutate() function deepcopies the genome argument
    it's handed and eventually returns a mutated genome.
   Every other function modifies the new (mutated) genome in place.

   Special Case: If the genome has no chomosomes,
    then it forces the mutation 'Insert Chomosome'.
   """
   mutated_genome = copy.deepcopy(genome) # make a copy of the DNA to mutate
   seed = random.randint(0,3)
   if len(mutated_genome) == 0: seed = 0
   if seed == 0:
      mutate_chromosome(mutated_genome)
   elif seed == 1:
      mutate_point(mutated_genome)
   elif seed == 2:
      mutate_color(mutated_genome)
   else: #seed ==3:
      mutate_opacity(mutated_genome)
   return mutated_genome

def mutate_chromosome(mutated_genome):
   """
   Chomosome Mutations
   These are actions that apply to chromosomes within the genome.
   Special Case: If the genome has 100 chromosomes,
    it will not 'insert chromosome'.
   This is effectively the maximum number of chromosomes.
   """
   seed = random.randint(0,5)
   if len(mutated_genome) <= 1: seed = 0
   if seed == 0:
      insert_chromosome(mutated_genome)
   elif seed == 1:
      remove_chromosome(mutated_genome)
   elif seed == 2:
      switch_chromosomes(mutated_genome)
   elif seed == 3:
      shuffle_chromosomes(mutated_genome)
   elif seed == 4:
      increment_chromosome(mutated_genome)
   else: #seed == 5:
      decrement_chromosome(mutated_genome)

def insert_chromosome(mutated_genome):
   """
   Insert Chromosome
   Inserts a chromosome with no points at a random index.
   This chromosome has a random color and opacity.
   """
   index = random.randint(0,len(mutated_genome))
   if color_mode == 'RGB':
      color_red = random.randint(0,255)
      color_green = random.randint(0,255)
      color_blue = random.randint(0,255)
      color = (color_red, color_blue, color_green)
   else: #color_mode == 'L':
      color = random.randint(0,255)
   opacity = random.randint(0,255)
   points = []
   mutated_genome.insert(index, [color,opacity,points])

def remove_chromosome(mutated_genome):
   """
   Remove Chromosome
   Removes a chromosome from a randomly chosen index.
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   del mutated_genome[index]

def switch_chromosomes(mutated_genome):
   """
   Switch Chromosomes
   Choses two random chromosomes and switches them in place.
   """
   index1 = random.randint(0,max(0,len(mutated_genome)-1))
   index2 = random.randint(0,max(0,len(mutated_genome)-1))
   temp = mutated_genome[index1]
   mutated_genome[index1] = mutated_genome[index2]
   mutated_genome[index2] = temp

def shuffle_chromosomes(mutated_genome):
   """
   Shuffle Chromosomes
   Shuffle the order of all chromosomes.
   """
   random.shuffle(mutated_genome)

def increment_chromosome(mutated_genome):
   """
   Increment Chromosome
   Choose a chromosome at random and move it up the list.
   This actually does one of three possible actions:
     1) move it up one location in the list
     2) move it up to a random location above it
     3) move it up to the top of the list
   """
   index1 = random.randint(0,max(0,len(mutated_genome)-2))
   seed = random.randint(0,2)
   if seed == 0:
      index2 = index1 + 1
   elif seed == 1:
      index2 = random.randint(index1,max(index1,len(mutated_genome)-1))
   else: #seed == 2:
      index2 = max(0,len(mutated_genome)-1)
   temp = mutated_genome[index1]
   mutated_genome[index1] = mutated_genome[index2]
   mutated_genome[index2] = temp

def decrement_chromosome(mutated_genome):
   """
   Decrement Chromosome
   Choose a chromosome at random and move it down the list.
   This actually does one of three possible actions:
     1) move it down one location in the list
     2) move it down to a random location below it
     3) move it down to the bottom of the list
   """
   index1 = random.randint(1,max(1,len(mutated_genome)-1))
   seed = random.randint(0,2)
   if seed == 0:
      index2 = index1 - 1
   elif seed == 1:
      index2 = random.randint(0, index1)
   else: #seed == 2:
      index2 = 0
   temp = mutated_genome[index1]
   mutated_genome[index1] = mutated_genome[index2]
   mutated_genome[index2] = temp

def mutate_point(mutated_genome):
   """
   Point Mutation
   These actions affect the size, shape,
    and location of the chromosomes' phenotype.
   The phenotype may be polygons, triangles, ellipses,
    circles, rectangles, diamonds, etc...
   """
   seed = random.randint(0,7)
   index = random.randint(0,max(0,len(mutated_genome)-1))
   if len(mutated_genome[index][2]) <= 3: seed = 0
   if seed == 0:
      insert_point(mutated_genome,index)
   elif seed == 1:
      remove_point(mutated_genome,index)
   elif seed == 2:
      switch_points(mutated_genome,index)
   elif seed == 3:
      shuffle_points(mutated_genome,index)
   elif seed == 4:
      move_point(mutated_genome,index)
   elif seed == 5:
      shift_point(mutated_genome,index)
   elif seed == 6:
      increment_point(mutated_genome,index)
   else: #seed == 7:
      decrement_point(mutated_genome,index)

def insert_point(mutated_genome,index):
   """
   Insert Point
   This randomly inserts a point. For polygons,
    this inserts a point randomly into its list of points.
   For ellipses and other phenotypes with a fixed number of points,
    this overwrites a randomly chosen with a new randomly placed point.
   """
   Xval = random.randint(-int(imagewidth/5.),int(imagewidth*6./5.))
   Yval = random.randint(-int(imageheight/5.),int(imageheight*6./5.))
   point = (Xval,Yval)
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])))
   mutated_genome[index][2].insert(point_index, point)

def remove_point(mutated_genome,index):
   """
   Remove Point
   This randomly removes a point. For polygons this removes a randomly
    selected point in the list of points.
   For ellipses and other phenotypes with a fixed number of points, this
    overwrites a randomly chosen point with a new randomly placed point.
   """
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   del mutated_genome[index][2][point_index]

def switch_points(mutated_genome,index):
   """
   Switch Points
   Chooses two points and randomly switches them in place.
   """
   point_index1 = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   point_index2 = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   temp = mutated_genome[index][2][point_index1]
   mutated_genome[index][2][point_index1] = mutated_genome[index][2][point_index2]
   mutated_genome[index][2][point_index2] = temp

def shuffle_points(mutated_genome,index):
   """
   Shuffle Points
   Shuffle the order of all points in place.
   """
   random.shuffle(mutated_genome[index][2])

def move_point(mutated_genome,index):
   """
   Move Point
   Chooses a point at random and moves it to a randomly chosen location.
    This can be anywhere on the image (or even slightly off of it).
   """
   Xval = random.randint(-int(imagewidth/5.),int(imagewidth*6./5.))
   Yval = random.randint(-int(imageheight/5.),int(imageheight*6./5.))
   point = (Xval,Yval)
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   mutated_genome[index][2][point_index] = point

def shift_point(mutated_genome,index):
   """
   Shift Point
   Chooses a point at random and moves it by a randomly selected amount.
   This amount is in general smaller than the image to make this
    a much more gradual move than Move Point.
   """
   Xval = random.randint(-int(imagewidth*0.1),int(imagewidth*0.1))
   Yval = random.randint(-int(imageheight*0.1),int(imageheight*0.1))
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   point = mutated_genome[index][2][point_index]
   newpoint = (point[0]+Xval,point[1]+Yval)
   mutated_genome[index][2][point_index] = newpoint

def increment_point(mutated_genome,index):
   """
   Increment Point
   Choose a point at random and move it up the list.
   """
   point_index1 = random.randint(0,max(0,len(mutated_genome[index][2])-2))
   seed = random.randint(0,2)
   if seed == 0:
      point_index2 = point_index1 + 1
   elif seed == 1:
      point_index2 = random.randint(point_index1,max(0,len(mutated_genome[index][2])-1))
   else: #seed == 2:
      point_index2 = max(0,len(mutated_genome[index][2])-1)
   temp = mutated_genome[index][2][point_index1]
   mutated_genome[index][2][point_index1] = mutated_genome[index][2][point_index2]
   mutated_genome[index][2][point_index2] = temp

def decrement_point(mutated_genome,index):
   """
   Decrement point
   Choose a point at random and move it down the list.
   """
   point_index1 = random.randint(1,max(0,len(mutated_genome[index][2])-1))
   seed = random.randint(0,2)
   if seed == 0:
      point_index2 = point_index1 - 1
   elif seed == 1:
      point_index2 = random.randint(0, point_index1)
   else: #seed == 2:
      point_index2 = 0
   temp = mutated_genome[index][2][point_index1]
   mutated_genome[index][2][point_index1] = mutated_genome[index][2][point_index2]
   mutated_genome[index][2][point_index2] = temp

def mutate_color(mutated_genome):
   """
   Color Mutations
   These actions only affect the color of the chromosomes.
   """
   seed = random.randint(0,2)
   if seed == 0:
      new_color(mutated_genome)
   elif seed == 1:
      change_color(mutated_genome)
   else: #seed == 2:
      switch_colors(mutated_genome)
   #else: seed == 3: # depricated
   #   shuffle_colors(mutated_genome)

def new_color(mutated_genome):
   """
   New Color
   This takes a chromosome and assigns it a completely random new color
    (regardless of the previous color).
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   if color_mode == 'RGB':
      color_red = random.randint(0,255)
      color_green = random.randint(0,255)
      color_blue = random.randint(0,255)
      color = (color_red, color_blue, color_green)
   else: #color_mode == 'L':
      color = random.randint(0,255)
   mutated_genome[index][0] = color

def change_color(mutated_genome):
   """
   Change Color
   This takes a chromosome and shifts its color values independently by a
    random (small) difference.
   The resulting color is very close to the original color (as opposed to
    'New Color').
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   if color_mode == 'RGB':
      color_red = random.randint(-25,25)
      color_green = random.randint(-25,25)
      color_blue = random.randint(-25,25)
      color = mutated_genome[index][0]
      newcolor = (color[0]+color_red,color[1]+color_green,color[2]+color_blue)
   else: #color_mode == 'L':
      color_diff = random.randint(-25,25)
      color = mutated_genome[index][0]
      newcolor = color+color_diff
   mutated_genome[index][0] = newcolor

def switch_colors(mutated_genome):
   """
   Switch Colors
   This picks two chromosomes at random and switches their colors.
   """
   index1 = random.randint(0,max(0,len(mutated_genome)-1))
   index2 = random.randint(0,max(0,len(mutated_genome)-1))
   temp = mutated_genome[index1][0]
   mutated_genome[index1][0] = mutated_genome[index2][0]
   mutated_genome[index2][0] = temp

def shuffle_colors(mutated_genome):
   """
   Shuffle Colors
   This takes the colors over every chromosome and 
    randomly shuffles all of them.
   Each chromosome gets a color that a chromosome had before
    (with each having equal probability).
   """
   mutated_genome

def mutate_opacity(mutated_genome):
   """
   Opacity Actions
   These actions only affect the opacity of the chromosomes.
   """
   seed = random.randint(0,2)
   if seed == 0:
      new_opacity(mutated_genome)
   elif seed == 1:
      change_opacity(mutated_genome)
   else: #seed == 2:
      switch_opacities(mutated_genome)
   #else: #seed == 3: # depricated
   #   shuffle_opacities(mutated_genome)

def new_opacity(mutated_genome):
   """
   New Opacity
   This takes a chromosome and assigns it a completely random new opacity
    (regardless of the previous opacity).
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   opacity = random.randint(0,255)
   mutated_genome[index][1] = opacity

def change_opacity(mutated_genome):
   """
   Change Opacity
   This takes a chromosome and shifts its opacity value 
    by a random (small) difference.
   The resulting color is very close to the original color 
    (as opposed to 'New Opacity').
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   opacity = random.randint(-25,25)
   mutated_genome[index][1] = opacity + mutated_genome[index][1]

def switch_opacities(mutated_genome):
   """
   Switch Opacities
   This picks two chromosomes at random and switches their colors.
   """
   index1 = random.randint(0,max(0,len(mutated_genome)-1))
   index2 = random.randint(0,max(0,len(mutated_genome)-1))
   temp = mutated_genome[index1][1]
   mutated_genome[index1][1] = mutated_genome[index2][1]
   mutated_genome[index2][1] = temp

def shuffle_opacities(mutated_genome):
   """
   Shuffle Opacities
   This takes the opacity over every chromosome and 
    randomly shuffles all of them.
   Each chromosome gets an opacity that a chromosome had before 
    (with each having equal probability).
   """
   mutated_genome   

