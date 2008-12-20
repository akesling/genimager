#!/usr/bin/python
#  Mutate Function
#   EXCLUSIVELY FOR POLYGONS
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
from math import pi, sin, cos
from poly_imager import random
global imagewidth, imageheight, color_mode

########################
## Probability Values ##
########################
## Chromosome Operations ##
# General Operations
increment_chromosome_range	= 1
trade_chromosome_range	= 1
trade_chromosome_sigma	= 2
switch_chromosome_range	= 1
switch_chromosome_sigma	= 5
change_chromosome_range = 1
# Chromosome Specific Operations
place_chromosome_range	= .1
put_chromosome_range	= .1
insert_chromosome_range	= .1
remove_chromosome_range = .1
## Shape Operations ##
# General Operations
increment_shape_range	= 1
trade_shape_range	= 1
trade_shape_sigma	= 2
switch_shape_range	= 1
switch_shape_sigma	= 5
change_shape_range	= 1
# Shape Specific Operations
step_shape_range	= 1
shift_shape_range	= 1
shift_shape_sigma	= 8
move_shape_range	= 1
move_shape_sigma	= 32
new_shape_range		= 1
place_shape_range	= 1
put_shape_range		= 1
insert_shape_range	= 1
remove_shape_range	= 1
## Color (Fill) Operations
# General Operations
increment_color_range	= 1
trade_color_range	= 1
trade_color_sigma	= 2
switch_color_range	= 1
switch_color_sigma	= 5
change_color_range	= 1
# Color Specific Operations
step_color_range	= 1
shift_color_range	= 1
shift_color_sigma	= 8
move_color_range	= 1
move_color_sigma	= 32
new_color_range		= 1
## Opacity (Fill) Operations
# General Operations
increment_opacity_range	= 1
trade_opacity_range	= 1
trade_opacity_sigma	= 2
switch_opacity_range	= 1
switch_opacity_sigma	= 5
change_opacity_range	= 1
# Opacity Specific Operations
step_opacity_range	= 1
shift_opacity_range	= 1
shift_opacity_sigma	= 8
move_opacity_range	= 1
move_opacity_sigma	= 32
new_opacity_range	= 1

## Mutate ##
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
   # make a copy of the genome, which will then be mutated in place
   mutated_genome = copy.deepcopy(genome)
   chromosome_range = sum(increment_chromosome_range, trade_chromosome_range, switch_chromosome_range, \
      change_chromosome_range, place_chromosome_range, put_chromosome_range, insert_chromosome_range, \
      remove_chromosome_range)
   shape_range = sum(increment_shape_range, trade_shape_range, switch_shape_range, change_shape_range, \
      step_shape_range, shift_shape_range, move_shape_range, new_shape_range, place_shape_range, \
      put_shape_range, insert_shape_range, remove_shape_range)
   color_range = sum(increment_color_range, trade_color_range, switch_color_range, change_color_range, \
      step_color_range, shift_color_range, move_color_range, new_color_range)
   opacity_range = sum(increment_opacity_range, trade_opacity_range, switch_opacity_range, change_opacity_range, \
      step_opacity_range, shift_opacity_range, move_opacity_range, new_opacity_range)
   shape_range_sum = shape_range + chromosome_range
   color_range_sum = color_range + shape_range_sum
   range = opacity_range + color_range_sum
   seed = random.uniform(0,range)
   if len(mutated_genome) == 0: seed = 0
   if seed < chromosome_range:
      mutate_chromosome(mutated_genome, seed)
   elif seed < shape_range_sum:
      seed = seed - chromosome_range
      mutate_shape(mutated_genome, seed)
   elif seed < color_range_sum:
      seed = seed - shape_range_sum
      mutate_color(mutated_genome, seed)
   else: #seed < range:
      seed = seed - color_range_sum
      mutate_opacity(mutated_genome, seed)
   return mutated_genome

## Mutate Chromosome ##
def mutate_chromosome(mutated_genome, seed):
   """
   Chomosome Mutations
   These are actions that apply to chromosomes within the genome.
   Special Case: If the genome has 100 chromosomes,
    it will not 'insert chromosome'.
   This is effectively the maximum number of chromosomes.
   """
   trade_chromosome_range_sum = increment_chromosome_range + trade_chromosome_range
   switch_chromosome_range_sum = switch_chromosome_range + trade_chromosome_range_sum
   change_chromosome_range_sum = change_chromosome_range + switch_chromosome_range_sum
   place_chromosome_range_sum = place_chromosome_range + change_chromosome_range_sum
   put_chromosome_range_sum = put_chromosome_range + place_chromosome_range_sum
   insert_chromosome_range_sum = insert_chromosome_range + put_chromosome_range_sum
   #remove_chromosome_range_sum = remove_chromosome_range + insert_chromosome_range_sum
   # force it to add a chromosome if there are none
   if len(mutated_genome) <= 1:
      place_chromosome(mutated_genome)
   elif seed < increment_chromosome_range:
      increment_chromosome(mutated_genome)
   elif seed < trade_chromosome_range_sum:
      trade_chromosome(mutated_genome)
   elif seed < switch_chromosome_range_sum:
      switch_chromosome(mutated_genome)
   elif seed < change_chromosome_range_sum:
      change_chromosome(mutated_genome)
   elif seed < place_chromosome_range_sum:
      place_chromosome(mutated_genome)
   elif seed < put_chromosome_range_sum:
      put_chromosome(mutated_genome)
   elif seed < insert_chromosome_range_sum:
      insert_chromosome(mutated_genome)
   else: #seed < remove_chromosome_range_sum:
      remove_chromosome(mutated_genome)

## Increment Chromosome ##
def increment_chromosome(mutated_genome):
   """
   Increment Chromosome
   Choose a chromosome at random and move it up or down
   the genome by one.
   """
   sign = random.randint(0,1)
   if len(mutated_genome) < 2: #theres only one item
      index1 = 0
      index2 = 0
   elif sign == 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = index1 + 1
   else: #sign == 1: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = index1 - 1
   temp = mutated_genome[index1]
   mutated_genome[index1] = mutated_genome[index2]
   mutated_genome[index2] = temp

## Trade Chromosome ##
def trade_chromosome(mutated_genome):
   """
   Trade Chromosome
   Choose a chromosome at random and move it up or down
   the genome by a small amount.
   """
   radius = int(random.gauss(0,trade_chromosome_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   temp = mutated_genome[index1]
   del mutated_genome[index1]
   mutated_genome.insert(index2, temp)

## Switch Chromosome ##
def switch_chromosome(mutated_genome):
   """
   Switch Chromosome
   Choose a chromosome at random and move it up or down
   the genome by a large amount.
   """
   radius = int(random.gauss(0,switch_chromosome_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   temp = mutated_genome[index1]
   del mutated_genome[index1]
   mutated_genome.insert(index2, temp)

## Change Chromosome ##
def change_chromosome(mutated_genome):
   """
   Chage Chromosome
   Choose a chromosome at random and move it to a random
   place in the genome
   """
   if len(mutated_genome) < 2: 
      index1 = 0
      index2 = 0
   else:
      index1 = random.randint(0,len(mutated_genome)-1)
      index2 = random.randint(0,len(mutated_genome)-1)
   temp = mutated_genome[index1]
   del mutated_genome[index1]
   mutated_genome.insert(index2, temp)

## Place Chromosome ##
def place_chromosome(mutated_genome):
   """
   Place Chromosome
   Inserts a small chromosome with 3 points at a random index.
   This chromosome has a random color and opacity.
   """
   index = random.randint(0,len(mutated_genome))
   fill = random_fill()
   shape = []
   shape.append(random_point())
   shape.append(near_point(shape[0]))
   shape.append(near_point(shape[0]))
   mutated_genome.insert(index, (fill,shape))

## Put Chromosome ##
def put_chromosome(mutated_genome):
   """
   Put Chromosome
   Inserts a large chromosome with 3 points at a random index.
   This chromosome has a random color and opacity.
   """
   index = random.randint(0,len(mutated_genome))
   fill = random_fill()
   shape = []
   shape.append(random_point())
   shape.append(far_point(shape[0]))
   shape.append(far_point(shape[0]))
   mutated_genome.insert(index, (fill,shape))

## Insert Chromosome ##
def insert_chromosome(mutated_genome):
   """
   Insert Chromosome
   Inserts a random chromosome with 3 points at a random index.
   This chromosome has a random color and opacity.
   """
   index = random.randint(0,len(mutated_genome))
   fill = random_fill()
   shape = []
   shape.append(random_point())
   shape.append(random_point())
   shape.append(random_point())
   mutated_genome.insert(index, (fill,shape))

## Remove Chromosome ##
def remove_chromosome(mutated_genome):
   """
   Remove Chromosome
   Removes a chromosome from a randomly chosen index.
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   del mutated_genome[index]


## Mutate shape ##
def mutate_shape(mutated_genome,seed):
   """
   Shape Mutation
   These actions affect the size, shape,
    and location of the chromosomes' phenotype.
   The phenotype is polygons
   """
   trade_shape_range_sum = increment_shape_range + trade_shape_range
   switch_shape_range_sum = switch_shape_range + trade_shape_range_sum
   change_shape_range_sum = change_shape_range + switch_shape_range_sum
   step_shape_range_sum = step_shape_range + change_shape_range_sum
   shift_shape_range_sum = shift_shape_range + step_shape_range_sum
   move_shape_range_sum = move_shape_range + shift_shape_range_sum
   new_shape_range_sum = new_shape_range + move_shape_range_sum
   place_shape_range_sum = place_shape_range + new_shape_range_sum
   put_shape_range_sum = put_shape_range + place_shape_range_sum
   insert_shape_range_sum = inset_shape_range + put_shape_range_sum
   #remove_shape_range_sum = remove_shape_range + insert_shape_range_sum
   if seed < increment_shape_range:
      increment_shape(mutated_genome)
   elif seed < trade_shape_range_sum:
      trade_shape(mutated_genome)
   elif seed < switch_shape_range_sum:
      switch_shape(mutated_genome)
   elif seed < change_shape_range_sum:
      change_shape(mutated_genome)
   elif seed < step_shape_range_sum:
      step_shape(mutated_genome)
   elif seed < shift_shape_range_sum:
      shift_shape(mutated_genome)
   elif seed < move_shape_range_sum:
      move_shape(mutated_genome)
   elif seed < new_shape_range_sum:
      new_shape(mutated_genome)
   elif seed < place_shape_range_sum:
      place_shape(mutated_genome)
   elif seed < put_shape_range_sum:
      put_shape(mutated_genome)
   elif seed < insert_shape_range_sum:
      insert_shape(mutated_genome)
   else: #seed < remove_shape_range_sum:
      remove_shape(mutated_genome)


## Increment Shape ##
def increment_shape(mutated_genome):
   """
   Increment Shape
   Choose a chromosome at random and move it's shape up or down
   the genome by one.
   """
   sign = random.randint(0,1)
   if len(mutated_genome) < 2: #theres only one item
      index1 = 0
      index2 = 0
   elif sign == 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = index1 + 1
   else: #sign == 1: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = index1 - 1
   newchromosome = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index2] = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index1] = newchromosome

## Trade Shape ##
def trade_shape(mutated_genome):
   """
   Trade Shape
   Choose a chromosome at random and move it's shape up or down
   the genome by a small amount.
   """
   radius = int(random.gauss(0,trade_shape_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   newchromosome = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index2] = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index1] = newchromosome

## Switch Shape ##
def switch_shape(mutated_genome):
   """
   Switch Shape
   Choose a chromosome at random and move it's shape up or down
   the genome by a large amount.
   """
   radius = int(random.gauss(0,switch_shape_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   newchromosome = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index2] = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index1] = newchromosome

## Change Shape ##
def change_shape(mutated_genome):
   """
   Chage Shape
   Choose a shape at random and move it to a random
   place in the genome
   """
   if len(mutated_genome) < 2: 
      index1 = 0
      index2 = 0
   else:
      index1 = random.randint(0,len(mutated_genome)-1)
      index2 = random.randint(0,len(mutated_genome)-1)
   newchromosome = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index2] = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index1] = newchromosome

## Step Shape ##
def step_shape(mutated_genome):
   """
   Step Shape
   Move a point coordinate by one.
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1]))
   point = mutated_genome[index][1][pointindex]
   axis = random.randint(0,1)
   sign = random.randint(0,1)
   if axis == 0 and sign == 0:
      newpoint = (point[0] + 1, point[1])
   elif axis == 0 and sign == 1:
      newpoint = (point[0] - 1, point[1])
   elif axis == 1 and sign == 0:
      newpoint = (point[0], point[1] + 1)
   elif axis == 1 and sign == 1:
      newpoint = (point[0], point[1] - 1)
   mutated_genome[index][1][pointindex] = newpoint

## Shift Shape ##
def shift_shape(mutated_genome):
   """
   Shift Shape
   Move a point coordinate by a small amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1]))
   point = mutated_genome[index][1][pointindex]
   newpoint = near_point(point)
   mutated_genome[index][1][pointindex] = newpoint

## Move Shape ##
def move_shape(mutated_genome):
   """
   Move Shape
   Move a point coordinate by a large amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1]))
   point = mutated_genome[index][1][pointindex]
   newpoint = far_point(point)
   mutated_genome[index][1][pointindex] = newpoint

## New Shape ##
def new_shape(mutated_genome):
   """
   New Shape
   Move a point coordinate to a random point
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1]))
   newpoint = random_point()
   mutated_genome[index][1][pointindex] = newpoint



## Need place, put, insert, remove shape/point and the rest
#############################################################

## Insert Point ##
def insert_point(mutated_genome,index):
   """
   Insert Point
   This randomly inserts a point. For polygons,
    this inserts a point randomly into its list of points.
   """
   Xval = random.randint(-int(imagewidth/5.),int(imagewidth*6./5.))
   Yval = random.randint(-int(imageheight/5.),int(imageheight*6./5.))
   point = (Xval,Yval)
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])))
   mutated_genome[index][2].insert(point_index, point)

## Remove Point ##
def remove_point(mutated_genome,index):
   """
   Remove Point
   This randomly removes a point. For polygons this removes a randomly
    selected point in the list of points.
   """
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   del mutated_genome[index][2][point_index]

## Switch Points ##
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

## Shuffle Points ##
def shuffle_points(mutated_genome,index):
   """
   Shuffle Points
   Shuffle the order of all points in place.
   """
   random.shuffle(mutated_genome[index][2])

## Move Point ##
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

## Shift Point ##
def shift_point(mutated_genome,index):
   """
   Shift Point
   Chooses a point at random and moves it by a randomly selected amount.
   This amount is in general smaller than the image to make this
    a much more gradual move than Move Point.
   """
   radius = random.gauss(0,shift_point_sigma*max(imageheight,imagewidth))
   angle = random.uniform(0,math.pi)
   Xval = radius*math.cos(angle)
   Yval = radius*math.sin(angle)
   point_index = random.randint(0,max(0,len(mutated_genome[index][2])-1))
   point = mutated_genome[index][2][point_index]
   newpoint = (point[0]+Xval,point[1]+Yval)
   mutated_genome[index][2][point_index] = newpoint

## Increment Point ##
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

## Decrement Point ##
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

## Mutate Color ##
def mutate_color(mutated_genome):
   """
   Color Mutations
   These actions only affect the color of the chromosomes.
   """
   change_color_range_sum = new_color_range + change_color_range
   range = switch_color_range + change_color_range_sum
   seed = random.uniform(0,range)
   if seed < new_color_range:
      new_color(mutated_genome)
   elif seed < change_color_range_sum:
      change_color(mutated_genome)
   else: #seed < range:
      switch_colors(mutated_genome)
   #else:  # depricated
   #   shuffle_colors(mutated_genome)

## New Color ##
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

## Change Color ##
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
      color_red = random.gauss(0, change_color_sigma)
      color_green = random.gauss(0, change_color_sigma)
      color_blue = random.randint(0, change_color_sigma)
      color = mutated_genome[index][0]
      newcolor = (color[0] + color_red, color[1] + color_green, color[2] + color_blue)
   else: #color_mode == 'L':
      color_diff = random.randint(0, change_color_sigma)
      color = mutated_genome[index][0]
      newcolor = color + color_diff
   mutated_genome[index][0] = newcolor

## Switch Colors ##
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

## Shuffle Colors - Depricated ##
def shuffle_colors(mutated_genome):
   """
   Shuffle Colors - DEPRICATED
   This takes the colors over every chromosome and 
    randomly shuffles all of them.
   Each chromosome gets a color that a chromosome had before
    (with each having equal probability).
   """
   mutated_genome

## Mutate Opacity ##
def mutate_opacity(mutated_genome):
   """
   Opacity Actions
   These actions only affect the opacity of the chromosomes.
   """
   change_opacity_range_sum = new_opacity_range + change_opacity_range
   range = switch_opacities_range + change_opacity_range_sum
   seed = random.uniform(0,range)
   if seed < new_opacity_range:
      new_opacity(mutated_genome)
   elif seed < change_opacity_range_sum:
      change_opacity(mutated_genome)
   else: #seed < range:
      switch_opacities(mutated_genome)
   #else: # depricated
   #   shuffle_opacities(mutated_genome)

## New Opacity ##
def new_opacity(mutated_genome):
   """
   New Opacity
   This takes a chromosome and assigns it a completely random new opacity
    (regardless of the previous opacity).
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   opacity = random.randint(0,255)
   mutated_genome[index][1] = opacity

## Change Opacity ##
def change_opacity(mutated_genome):
   """
   Change Opacity
   This takes a chromosome and shifts its opacity value 
    by a random (small) difference.
   The resulting color is very close to the original color 
    (as opposed to 'New Opacity').
   """
   index = random.randint(0,max(0,len(mutated_genome)-1))
   opacity = random.gauss(0,change_opacity_sigma)
   mutated_genome[index][1] = opacity + mutated_genome[index][1]

## Switch Opacities ##
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

## Shuffle Opacities - Depricated##
def shuffle_opacities(mutated_genome):
   """
   Shuffle Opacities - DEPRICATED
   This takes the opacity over every chromosome and 
    randomly shuffles all of them.
   Each chromosome gets an opacity that a chromosome had before 
    (with each having equal probability).
   """
   mutated_genome   

## Random Color ##
def random_color():
   """
   Random Color
   Generate a random color
   returns a 3-tuple (R,G,B) for color
   and an int for grayscale
   """
   if color_mode == 'RGB':
      color_red = random.randint(0,255)
      color_green = random.randint(0,255)
      color_blue = random.randint(0,255)
      return (color_red, color_green, color_blue)
   else: #color_mode == 'L':
      color_grayscale = random.randint(0,255)
      return color_grayscale

## Near Color ##
def near_color(oldcolor):
   """
   Near Color
   Generate a color close to a given color
   color is given as a 3-tuple for color and int for grayscale
   """
   if color_mode == 'RGB':
      color_red = int(random.gauss(0, shift_color_sigma))
      color_green = int(random.gauss(0, shift_color_sigma))
      color_blue = int(random.randint(0, shift_color_sigma))
      newcolor = (oldcolor[0] + color_red, oldcolor[1] + color_green, oldcolor[2] + color_blue)
      return newcolor
   else: #color_mode == 'L':
      color_diff = int(random.randint(0, shift_color_sigma))
      newcolor = oldcolor + color_diff
      return newcolor

## Far Color ##
def far_color(oldcolor):
   """
   Far Color
   Generate a color far from a given color
   color is given as a 3-tuple for color and int for grayscale
   """
   if color_mode == 'RGB':
      color_red = int(random.gauss(0, move_color_sigma))
      color_green = int(random.gauss(0, move_color_sigma))
      color_blue = int(random.randint(0, move_color_sigma))
      newcolor = (oldcolor[0] + color_red, oldcolor[1] + color_green, oldcolor[2] + color_blue)
      return newcolor
   else: #color_mode == 'L':
      color_diff = int(random.randint(0, move_color_sigma))
      newcolor = oldcolor + color_diff
      return newcolor

## Random Opacity ##
def random_opacity():
   """
   Random Opacity
   Generate a random opacity
   """
   opacity = random.randint(0,255)
   return opacity

## Near Opacity ##
def near_opacity(oldopacity):
   """
   Near Color
   Generate an opacity close to a given opacity
   """
   opacity_diff = int(random.randint(0, shift_opacity_sigma))
   newopacity = oldopacity + opacity_diff
   return newopacity

## Far Opacity ##
def far_opacity(oldopacity):
   """
   Far Color
   Generate an opacity far from a given opacity
   """
   opacity_diff = int(random.randint(0, move_opacity_sigma))
   newopacity = oldopacity + opacity_diff
   return newopacity

## Random Point ##
def random_point():
   """
   Random Point
   Generate a random point on the image (x,y)
   """
   Xval = random.randint(-int(imagewidth/5.),int(imagewidth*6./5.))
   Yval = random.randint(-int(imageheight/5.),int(imageheight*6./5.))
   point = (Xval,Yval)
   return point

## Near Point ##
def near_point(oldpoint):
   """
   Near Point
   Generate a point near a given point
   """
   radius = random.gauss(0,shift_point_sigma*sum(imageheight,imagewidth)/2.)
   angle = random.uniform(0,pi)
   Xval = radius*cos(angle)
   Yval = radius*sin(angle)
   newpoint = (oldpoint[0]+Xval,oldpoint[1]+Yval)
   return newpoint
   
## Far Point ##
def far_point(oldpoint):
   """
   Far Point
   Generate a point far from a given point
   """
   radius = random.gauss(0,move_point_sigma*sum(imageheight,imagewidth)/2.)
   angle = random.uniform(0,pi)
   Xval = radius*cos(angle)
   Yval = radius*sin(angle)
   newpoint = (oldpoint[0]+Xval,oldpoint[1]+Yval)
   return newpoint

## Random Fill ##
def random_fill():
   """
   Random Fill
   Returns a random Fill appropriate for the color_mode
   """
   color = random_color()
   opacity = random_opacity()
   if color_mode == 'RGB'
      fill = (color[0], color[1], color[2], opacity)
      return fill
   else: #color_mode == 'L':
      fill = (color, opacity)
      return fill

