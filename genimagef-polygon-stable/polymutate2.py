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
import copy, random
from math import pi, sin, cos
global imagewidth, imageheight, color_mode

## Maxima ##
max_chromosomes = 255
max_points = 255

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
increment_point_range	= 1
trade_point_range	= 1
trade_point_sigma	= 2
switch_point_range	= 1
switch_point_sigma	= 5
change_point_range	= 1
step_point_range	= 1
shift_point_range	= 1
shift_point_sigma	= 8
move_point_range	= 1
move_point_sigma	= 32
new_point_range		= 1
place_point_range	= 1
put_point_range		= 1
insert_point_range	= 1
remove_point_range	= 1
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
   chromosome_range = increment_chromosome_range + trade_chromosome_range + switch_chromosome_range + \
      change_chromosome_range + place_chromosome_range + put_chromosome_range + insert_chromosome_range + \
      remove_chromosome_range
   shape_range = increment_shape_range + trade_shape_range + switch_shape_range + change_shape_range + \
      increment_point_range + trade_point_range + switch_point_range + change_point_range + \
      step_point_range + shift_point_range + move_point_range + new_point_range + place_point_range + \
      put_point_range + insert_point_range + remove_point_range
   color_range = increment_color_range + trade_color_range + switch_color_range + change_color_range + \
      step_color_range + shift_color_range + move_color_range + new_color_range
   opacity_range = increment_opacity_range + trade_opacity_range + switch_opacity_range + change_opacity_range + \
      step_opacity_range + shift_opacity_range + move_opacity_range + new_opacity_range
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
   if len(mutated_genome) <= max_chromosomes:
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
   if len(mutated_genome) <= max_chromosomes:
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
   if len(mutated_genome) <= max_chromosomes:
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
   increment_point_range_sum = change_shape_range_sum + increment_point_range
   trade_point_range_sum = increment_point_range + trade_point_range
   switch_point_range_sum = switch_point_range + trade_point_range_sum
   change_point_range_sum = change_point_range + switch_point_range_sum
   step_point_range_sum = step_point_range + change_point_range_sum
   shift_point_range_sum = shift_point_range + step_point_range_sum
   move_point_range_sum = move_point_range + shift_point_range_sum
   new_point_range_sum = new_point_range + move_point_range_sum
   place_point_range_sum = place_point_range + new_point_range_sum
   put_point_range_sum = put_point_range + place_point_range_sum
   insert_point_range_sum = insert_point_range + put_point_range_sum
   #remove_point_range_sum = remove_point_range + insert_point_range_sum
   if seed < increment_shape_range:
      increment_shape(mutated_genome)
   elif seed < trade_shape_range_sum:
      trade_shape(mutated_genome)
   elif seed < switch_shape_range_sum:
      switch_shape(mutated_genome)
   elif seed < change_shape_range_sum:
      change_shape(mutated_genome)
   elif seed < increment_point_range_sum:
      increment_point(mutated_genome)
   elif seed < trade_point_range_sum:
      trade_point(mutated_genome)
   elif seed < switch_point_range_sum:
      switch_point(mutated_genome)
   elif seed < change_point_range_sum:
      change_point(mutated_genome)
   elif seed < step_point_range_sum:
      step_point(mutated_genome)
   elif seed < shift_point_range_sum:
      shift_point(mutated_genome)
   elif seed < move_point_range_sum:
      move_point(mutated_genome)
   elif seed < new_point_range_sum:
      new_point(mutated_genome)
   elif seed < place_point_range_sum:
      place_point(mutated_genome)
   elif seed < put_point_range_sum:
      put_point(mutated_genome)
   elif seed < insert_point_range_sum:
      insert_point(mutated_genome)
   else: #seed < remove_point_range_sum:
      remove_point(mutated_genome)


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

## Increment Point ##
def increment_point(mutated_genome):
   """
   Increment Point
   Choose a chromosome at random and move a point in it up or down
   the by one.
   """
   sign = random.randint(0,1)
   index = random.randint(0,len(mutated_genome)-1)
   if len(mutated_genome[index][1]) < 2: #theres only one point
      index1 = 0
      index2 = 0
   elif sign == 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome[index][1])-2)
      index2 = index1 + 1
   else: #sign == 1: # move it down the list
      index1 = random.randint(1,len(mutated_genome[index][1])-1)
      index2 = index1 - 1
   temp = mutated_genome[index][1][index1]
   del mutated_genome[index][1][index1]
   mutated_genome[index][1].insert(index2, temp)

## Trade Point ##
def trade_point(mutated_genome):
   """
   Trade Point
   Choose a chromosome at random and move a point up or down
   by a small amount.
   """
   index = random.randint(0,len(mutated_genome)-1)
   radius = int(random.gauss(0,trade_point_sigma))
   if len(mutated_genome[index][1]) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome[index][1])-2)
      index2 = min(index1 + radius, len(mutated_genome[index][1])-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome[index][1])-1)
      index2 = max(index1 + radius, len(mutated_genome[index][1])-2)
   temp = mutated_genome[index][1][index1]
   del mutated_genome[index][1][index1]
   mutated_genome[index][1].insert(index2, temp)

## Switch Point ##
def switch_point(mutated_genome):
   """
   Switch Point
   Choose a chromosome at random and move a point up or down
   by a small amount.
   """
   index = random.randint(0,len(mutated_genome)-1)
   radius = int(random.gauss(0,switch_point_sigma))
   if len(mutated_genome[index][1]) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome[index][1])-2)
      index2 = min(index1 + radius, len(mutated_genome[index][1])-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome[index][1])-1)
      index2 = max(index1 + radius, len(mutated_genome[index][1])-2)
   temp = mutated_genome[index][1][index1]
   del mutated_genome[index][1][index1]
   mutated_genome[index][1].insert(index2, temp)

## Change Point ##
def change_point(mutated_genome):
   """
   Chage Point
   Choose a shape at random and move a point in it to a random
   place in the list
   """
   index = random.randint(0,len(mutated_genome)-1)
   if len(mutated_genome[index][1]) < 2: 
      index1 = 0
      index2 = 0
   else:
      index1 = random.randint(0,len(mutated_genome[index][1])-1)
      index2 = random.randint(0,len(mutated_genome[index][1])-1)
   temp = mutated_genome[index][1][index1]
   del mutated_genome[index][1][index1]
   mutated_genome[index][1].insert(index2, temp)

## Step Point ##
def step_point(mutated_genome):
   """
   Step Point
   Move a point coordinate by one.
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1])-1)
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

## Shift Point ##
def shift_point(mutated_genome):
   """
   Shift Point
   Move a point coordinate by a small amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1])-1)
   point = mutated_genome[index][1][pointindex]
   newpoint = near_point(point)
   mutated_genome[index][1][pointindex] = newpoint

## Move Point ##
def move_point(mutated_genome):
   """
   Move Point
   Move a point coordinate by a large amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1])-1)
   point = mutated_genome[index][1][pointindex]
   newpoint = far_point(point)
   mutated_genome[index][1][pointindex] = newpoint

## New Point ##
def new_point(mutated_genome):
   """
   New Point
   Move a point coordinate to a random point
   """
   index = random.randint(0,len(mutated_genome)-1)
   pointindex = random.randint(0,len(mutated_genome[index][1])-1)
   newpoint = random_point()
   mutated_genome[index][1][pointindex] = newpoint

## Put Point ##
def put_point(mutated_genome):
   """
   Put Point
   Put a new point coordinate close to an existing one.
   """
   index = random.randint(0,len(mutated_genome)-1)
   if len(mutated_genome[index][1]) <= max_points:
      pointindex = random.randint(0,len(mutated_genome[index][1])-1)
      point = mutated_genome[index][1][pointindex]
      newpoint = near_point(point)
      mutated_genome[index][1].insert(pointindex, newpoint)

## Place Point ##
def place_point(mutated_genome):
   """
   Place Point
   Put a new point coordinate far from to an existing one.
   """
   index = random.randint(0,len(mutated_genome)-1)
   if len(mutated_genome[index][1]) <= max_points:
      pointindex = random.randint(0,len(mutated_genome[index][1])-1)
      point = mutated_genome[index][1][pointindex]
      newpoint = far_point(point)
      mutated_genome[index][1].insert(pointindex, newpoint)

## Insert Point ##
def insert_point(mutated_genome):
   """
   Insert Point
   Put a new point coordinate at random
   """
   index = random.randint(0,len(mutated_genome)-1)
   if len(mutated_genome[index][1]) <= max_points:
      pointindex = random.randint(0,len(mutated_genome[index][1])-1)
      point = mutated_genome[index][1][pointindex]
      newpoint = random_point()
      mutated_genome[index][1].insert(pointindex, newpoint)

## Remove Point ##
def remove_point(mutated_genome):
   """
   Remove Point
   Remove a point coordinate at random
   """
   index = random.randint(0,len(mutated_genome)-1)
   if len(mutated_genome[index][1]) > 3:
      pointindex = random.randint(0,len(mutated_genome[index][1])-1)
      del mutated_genome[index][1][pointindex]

## Mutate Color ##
def mutate_color(mutated_genome,seed):
   """
   Color Mutations
   These actions only affect the color of the chromosomes.
   """
   trade_color_range_sum = increment_color_range + trade_color_range
   switch_color_range_sum = switch_color_range + trade_color_range_sum
   change_color_range_sum = change_color_range + switch_color_range_sum
   step_color_range_sum = step_color_range + change_color_range_sum
   shift_color_range_sum = shift_color_range + step_color_range_sum
   move_color_range_sum = move_color_range + shift_color_range_sum
   #new_color_range_sum = new_color_range + move_color_range_sum
   if seed < increment_color_range:
      increment_color(mutated_genome)
   elif seed < trade_color_range_sum:
      trade_color(mutated_genome)
   elif seed < switch_color_range_sum:
      switch_color(mutated_genome)
   elif seed < change_color_range_sum:
      change_color(mutated_genome)
   elif seed < step_color_range_sum:
      step_color(mutated_genome)
   elif seed < shift_color_range_sum:
      shift_color(mutated_genome)
   elif seed < move_color_range_sum:
      move_color(mutated_genome)
   else: #seed < new_color_range_sum:
      new_color(mutated_genome)

## Increment Color ##
def increment_color(mutated_genome):
   """
   Increment Color
   Choose a chromosome at random and move it's color up or down
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
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Trade Color ##
def trade_color(mutated_genome):
   """
   Trade Color
   Choose a chromosome at random and move it's color up or down
   the genome by a small amount.
   """
   radius = int(random.gauss(0,trade_color_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Switch Color ##
def switch_color(mutated_genome):
   """
   Switch Color
   Choose a chromosome at random and move it's color up or down
   the genome by a large amount.
   """
   radius = int(random.gauss(0,switch_color_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Change Color ##
def change_color(mutated_genome):
   """
   Chage Color
   Choose a Color at random and move it to a random
   place in the genome
   """
   if len(mutated_genome) < 2: 
      index1 = 0
      index2 = 0
   else:
      index1 = random.randint(0,len(mutated_genome)-1)
      index2 = random.randint(0,len(mutated_genome)-1)
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Step Color ##
def step_color(mutated_genome):
   """
   Step Color
   Move a color value by one.
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = mutated_genome[index][0]
   if len(fill) == 4: # R,G,B,A
      color = [fill[0],fill[1],fill[2]]
      axis = random.randint(0,2)
      sign = random.randint(0,1)
      if sign == 0:
         color[axis] = min(color[axis] + 1,255)
      else: #sign == 1: 
         color[axis] = max(color[axis] - 1,0)
      newfill = (color[0],color[1],color[2],fill[3])
   else: #len(fill) == 2: # L, A
      color = fill[0]
      sign = random.randint(0,1)
      if sign == 0:
         color = min(color + 1,255)
      else: #sign == 1: 
         color = max(color - 1,0)
      newfill = (color,fill[1])
   mutated_genome[index] = (newfill,mutated_genome[index][1])

## Shift Color ##
def shift_color(mutated_genome):
   """
   Shift Color
   Move a color value by a small amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = mutated_genome[index][0]
   if len(fill) == 4: # R,G,B,A
      color = (fill[0],fill[1],fill[2])
      newcolor = near_color(color)
      newfill = (newcolor[0],newcolor[1],newcolor[2],fill[3])
   else: #len(fill) == 2: # L,A
      color = fill[0]
      newcolor = near_color(color)
      newfill = (newcolor, fill[1])
   mutated_genome[index] = (newfill,mutated_genome[index][1])

## Move Color ##
def move_color(mutated_genome):
   """
   Move color
   Move a color value by a large amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = mutated_genome[index][0]
   if len(fill) == 4: # R,G,B,A
      color = (fill[0],fill[1],fill[2])
      newcolor = far_color(color)
      newfill = (newcolor[0],newcolor[1],newcolor[2],fill[3])
   else: #len(fill) == 2: # L,A
      color = fill[0]
      newcolor = far_color(color)
      newfill = (newcolor, fill[1])
   mutated_genome[index] = (newfill,mutated_genome[index][1])

## New Color ##
def new_color(mutated_genome):
   """
   New Color
   Move a color value to a random value
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = mutated_genome[index][0]
   if len(fill) == 4: # R,G,B,A
      newcolor = random_color()
      newfill = (newcolor[0],newcolor[1],newcolor[2],fill[3])
   else: #len(fill) == 2: # L,A
      newcolor = random_color()
      newfill = (newcolor, fill[1])
   mutated_genome[index] = (newfill,mutated_genome[index][1])













##########################################


## Mutate Opacity ##
def mutate_opacity(mutated_genome,seed):
   """
   Opacity Mutations
   These actions only affect the opacity of the chromosomes.
   """
   trade_opacity_range_sum = increment_opacity_range + trade_opacity_range
   switch_opacity_range_sum = switch_opacity_range + trade_opacity_range_sum
   change_opacity_range_sum = change_opacity_range + switch_opacity_range_sum
   step_opacity_range_sum = step_opacity_range + change_opacity_range_sum
   shift_opacity_range_sum = shift_opacity_range + step_opacity_range_sum
   move_opacity_range_sum = move_opacity_range + shift_opacity_range_sum
   #new_opacity_range_sum = new_opacity_range + move_opacity_range_sum
   if seed < increment_opacity_range:
      increment_opacity(mutated_genome)
   elif seed < trade_opacity_range_sum:
      trade_opacity(mutated_genome)
   elif seed < switch_opacity_range_sum:
      switch_opacity(mutated_genome)
   elif seed < change_opacity_range_sum:
      change_opacity(mutated_genome)
   elif seed < step_opacity_range_sum:
      step_opacity(mutated_genome)
   elif seed < shift_opacity_range_sum:
      shift_opacity(mutated_genome)
   elif seed < move_opacity_range_sum:
      move_opacity(mutated_genome)
   else: #seed < new_opacity_range_sum:
      new_opacity(mutated_genome)

## Increment opacity ##
def increment_opacity(mutated_genome):
   """
   Increment opacity
   Choose a chromosome at random and move it's opacity up or down
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
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Trade opacity ##
def trade_opacity(mutated_genome):
   """
   Trade opacity
   Choose a chromosome at random and move it's opacity up or down
   the genome by a small amount.
   """
   radius = int(random.gauss(0,trade_opacity_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Switch opacity ##
def switch_opacity(mutated_genome):
   """
   Switch opacity
   Choose a chromosome at random and move it's opacity up or down
   the genome by a large amount.
   """
   radius = int(random.gauss(0,switch_opacity_sigma))
   if len(mutated_genome) < 2 or radius == 0: 
      index1 = 0
      index2 = 0
   elif radius > 0: #move it up the list
      index1 = random.randint(0,len(mutated_genome)-2)
      index2 = min(index1 + radius, len(mutated_genome)-1)
   else: #radius < 0: # move it down the list
      index1 = random.randint(1,len(mutated_genome)-1)
      index2 = max(index1 + radius, len(mutated_genome)-2)
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Change opacity ##
def change_opacity(mutated_genome):
   """
   Chage opacity
   Choose a opacity at random and move it to a random
   place in the genome
   """
   if len(mutated_genome) < 2: 
      index1 = 0
      index2 = 0
   else:
      index1 = random.randint(0,len(mutated_genome)-1)
      index2 = random.randint(0,len(mutated_genome)-1)
   newchromosome = (mutated_genome[index2][0],mutated_genome[index1][1])
   mutated_genome[index2] = (mutated_genome[index1][0],mutated_genome[index2][1])
   mutated_genome[index1] = newchromosome

## Step opacity ##
def step_opacity(mutated_genome):
   """
   Step opacity
   Move a opacity value by one.
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = list(mutated_genome[index][0])
   opacity = fill.pop()
   sign = random.randint(0,1)
   if sign == 0:
      opacity += 1
      fill.append(opacity)
   else: #sign == 0:
      opacity -= 1
      fill.append(opacity)
   mutated_genome[index] = (tuple(fill),mutated_genome[index][1])

## Shift opacity ##
def shift_opacity(mutated_genome):
   """
   Shift opacity
   Move a opacity value by a small amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = list(mutated_genome[index][0])
   opacity = fill.pop()
   newopacity = near_opacity(opacity)
   fill.append(newopacity)
   mutated_genome[index] = (tuple(fill),mutated_genome[index][1])

## Move opacity ##
def move_opacity(mutated_genome):
   """
   Move opacity
   Move a opacity value by a large amount
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = list(mutated_genome[index][0])
   opacity = fill.pop()
   newopacity = far_opacity(opacity)
   fill.append(newopacity)
   mutated_genome[index] = (tuple(fill),mutated_genome[index][1])

## New opacity ##
def new_opacity(mutated_genome):
   """
   New opacity
   Move a opacity value to a random value
   """
   index = random.randint(0,len(mutated_genome)-1)
   fill = list(mutated_genome[index][0])
   opacity = fill.pop()
   newopacity = random_opacity()
   fill.append(newopacity)
   mutated_genome[index] = (tuple(fill),mutated_genome[index][1])




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
   radius = random.gauss(0,shift_point_sigma*(imageheight+imagewidth)/2.)
   angle = random.uniform(0,pi)
   Xval = int(radius*cos(angle))
   Yval = int(radius*sin(angle))
   newpoint = (oldpoint[0]+Xval,oldpoint[1]+Yval)
   return newpoint
   
## Far Point ##
def far_point(oldpoint):
   """
   Far Point
   Generate a point far from a given point
   """
   radius = random.gauss(0,move_point_sigma*(imageheight+imagewidth)/2.)
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
   if color_mode == 'RGB':
      fill = (color[0], color[1], color[2], opacity)
      return fill
   else: #color_mode == 'L':
      fill = (color, opacity)
      return fill

