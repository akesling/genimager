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
from __main__ import ImageWidth, ImageHeight, random, colormode

def mutate(DNA):
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
   mDNA = copy.deepcopy(DNA) # make a copy of the DNA to mutate
   seed = random.randint(0,3)
   if len(mDNA) == 0: seed = 0
   if seed == 0:
      mutate_chromosome(mDNA)
   elif seed == 1:
      mutate_point(mDNA)
   elif seed == 2:
      mutate_color(mDNA)
   else: #seed ==3:
      mutate_opacity(mDNA)
   return mDNA

def mutate_chromosome(mDNA):
   """
   Chomosome Mutations
   These are actions that apply to chromosomes within the genome.
   Special Case: If the genome has 100 chromosomes,
    it will not 'insert chromosome'.
   This is effectively the maximum number of chromosomes.
   """
   seed = random.randint(0,5)
   if len(mDNA) <= 1: seed = 0
   if seed == 0:
      insert_chromosome(mDNA)
   elif seed == 1:
      remove_chromosome(mDNA)
   elif seed == 2:
      switch_chromosomes(mDNA)
   elif seed == 3:
      shuffle_chromosomes(mDNA)
   elif seed == 4:
      increment_chromosome(mDNA)
   else: #seed == 5:
      decrement_chromosome(mDNA)

def insert_chromosome(mDNA):
   """
   Insert Chromosome
   Inserts a chromosome with no points at a random index.
   This chromosome has a random color and opacity.
   """
   index = random.randint(0,len(mDNA))
   if colormode == 'RGB':
      color_red = random.randint(0,255)
      color_green = random.randint(0,255)
      color_blue = random.randint(0,255)
      color = (color_red, color_blue, color_green)
   else: #colormode == 'L':
      color = random.randint(0,255)
   opacity = random.randint(0,255)
   points = []
   mDNA.insert(index, [color,opacity,points])

def remove_chromosome(mDNA):
   """
   Remove Chromosome
   Removes a chromosome from a randomly chosen index.
   """
   index = random.randint(0,max(0,len(mDNA)-1))
   del mDNA[index]

def switch_chromosomes(mDNA):
   """
   Switch Chromosomes
   Choses two random chromosomes and switches them in place.
   """
   index1 = random.randint(0,max(0,len(mDNA)-1))
   index2 = random.randint(0,max(0,len(mDNA)-1))
   temp = mDNA[index1]
   mDNA[index1] = mDNA[index2]
   mDNA[index2] = temp

def shuffle_chromosomes(mDNA):
   """
   Shuffle Chromosomes
   Shuffle the order of all chromosomes.
   """
   random.shuffle(mDNA)

def increment_chromosome(mDNA):
   """
   Increment Chromosome
   Choose a chromosome at random and move it up the list.
   This actually does one of three possible actions:
     1) move it up one location in the list
     2) move it up to a random location above it
     3) move it up to the top of the list
   """
   index1 = random.randint(0,max(0,len(mDNA)-2))
   seed = random.randint(0,2)
   if seed == 0:
      index2 = index1 + 1
   elif seed == 1:
      index2 = random.randint(index1,max(index1,len(mDNA)-1))
   else: #seed == 2:
      index2 = max(0,len(mDNA)-1)
   temp = mDNA[index1]
   mDNA[index1] = mDNA[index2]
   mDNA[index2] = temp

def decrement_chromosome(mDNA):
   """
   Decrement Chromosome
   Choose a chromosome at random and move it down the list.
   This actually does one of three possible actions:
     1) move it down one location in the list
     2) move it down to a random location below it
     3) move it down to the bottom of the list
   """
   index1 = random.randint(1,max(1,len(mDNA)-1))
   seed = random.randint(0,2)
   if seed == 0:
      index2 = index1 - 1
   elif seed == 1:
      index2 = random.randint(0, index1)
   else: #seed == 2:
      index2 = 0
   temp = mDNA[index1]
   mDNA[index1] = mDNA[index2]
   mDNA[index2] = temp

def mutate_point(mDNA):
   """
   Point Mutation
   These actions affect the size, shape,
    and location of the chromosomes' phenotype.
   The phenotype may be polygons, triangles, ellipses,
    circles, rectangles, diamonds, etc...
   """
   seed = random.randint(0,7)
   index = random.randint(0,max(0,len(mDNA)-1))
   if len(mDNA[index][2]) <= 3: seed = 0
   if seed == 0:
      insert_point(mDNA,index)
   elif seed == 1:
      remove_point(mDNA,index)
   elif seed == 2:
      switch_points(mDNA,index)
   elif seed == 3:
      shuffle_points(mDNA,index)
   elif seed == 4:
      move_point(mDNA,index)
   elif seed == 5:
      shift_point(mDNA,index)
   elif seed == 6:
      increment_point(mDNA,index)
   else: #seed == 7:
      decrement_point(mDNA,index)

def insert_point(mDNA,index):
   """
   Insert Point
   This randomly inserts a point. For polygons,
    this inserts a point randomly into its list of points.
   For ellipses and other phenotypes with a fixed number of points,
    this overwrites a randomly chosen with a new randomly placed point.
   """
   Xval = random.randint(-int(ImageWidth/5.),int(ImageWidth*6./5.))
   Yval = random.randint(-int(ImageHeight/5.),int(ImageHeight*6./5.))
   point = (Xval,Yval)
   point_index = random.randint(0,max(0,len(mDNA[index][2])))
   mDNA[index][2].insert(point_index, point)

def remove_point(mDNA,index):
   """
   Remove Point
   This randomly removes a point. For polygons this removes a randomly
    selected point in the list of points.
   For ellipses and other phenotypes with a fixed number of points, this
    overwrites a randomly chosen point with a new randomly placed point.
   """
   point_index = random.randint(0,max(0,len(mDNA[index][2])-1))
   del mDNA[index][2][point_index]

def switch_points(mDNA,index):
   """
   Switch Points
   Chooses two points and randomly switches them in place.
   """
   point_index1 = random.randint(0,max(0,len(mDNA[index][2])-1))
   point_index2 = random.randint(0,max(0,len(mDNA[index][2])-1))
   temp = mDNA[index][2][point_index1]
   mDNA[index][2][point_index1] = mDNA[index][2][point_index2]
   mDNA[index][2][point_index2] = temp

def shuffle_points(mDNA,index):
   """
   Shuffle Points
   Shuffle the order of all points in place.
   """
   random.shuffle(mDNA[index][2])

def move_point(mDNA,index):
   """
   Move Point
   Chooses a point at random and moves it to a randomly chosen location.
    This can be anywhere on the image (or even slightly off of it).
   """
   Xval = random.randint(-int(ImageWidth/5.),int(ImageWidth*6./5.))
   Yval = random.randint(-int(ImageHeight/5.),int(ImageHeight*6./5.))
   point = (Xval,Yval)
   point_index = random.randint(0,max(0,len(mDNA[index][2])-1))
   mDNA[index][2][point_index] = point

def shift_point(mDNA,index):
   """
   Shift Point
   Chooses a point at random and moves it by a randomly selected amount.
   This amount is in general smaller than the image to make this
    a much more gradual move than Move Point.
   """
   Xval = random.randint(-int(ImageWidth*0.1),int(ImageWidth*0.1))
   Yval = random.randint(-int(ImageHeight*0.1),int(ImageHeight*0.1))
   point_index = random.randint(0,max(0,len(mDNA[index][2])-1))
   point = mDNA[index][2][point_index]
   newpoint = (point[0]+Xval,point[1]+Yval)
   mDNA[index][2][point_index] = newpoint

def increment_point(mDNA,index):
   """
   Increment Point
   Choose a point at random and move it up the list.
   """
   point_index1 = random.randint(0,max(0,len(mDNA[index][2])-2))
   seed = random.randint(0,2)
   if seed == 0:
      point_index2 = point_index1 + 1
   elif seed == 1:
      point_index2 = random.randint(point_index1,max(0,len(mDNA[index][2])-1))
   else: #seed == 2:
      point_index2 = max(0,len(mDNA[index][2])-1)
   temp = mDNA[index][2][point_index1]
   mDNA[index][2][point_index1] = mDNA[index][2][point_index2]
   mDNA[index][2][point_index2] = temp

def decrement_point(mDNA,index):
   """
   Decrement point
   Choose a point at random and move it down the list.
   """
   point_index1 = random.randint(1,max(0,len(mDNA[index][2])-1))
   seed = random.randint(0,2)
   if seed == 0:
      point_index2 = point_index1 - 1
   elif seed == 1:
      point_index2 = random.randint(0, point_index1)
   else: #seed == 2:
      point_index2 = 0
   temp = mDNA[index][2][point_index1]
   mDNA[index][2][point_index1] = mDNA[index][2][point_index2]
   mDNA[index][2][point_index2] = temp

def mutate_color(mDNA):
   """
   Color Mutations
   These actions only affect the color of the chromosomes.
   """
   seed = random.randint(0,2)
   if seed == 0:
      new_color(mDNA)
   elif seed == 1:
      change_color(mDNA)
   else: #seed == 2:
      switch_colors(mDNA)
   #else: seed == 3: # depricated
   #   shuffle_colors(mDNA)

def new_color(mDNA):
   """
   New Color
   This takes a chromosome and assigns it a completely random new color
    (regardless of the previous color).
   """
   index = random.randint(0,max(0,len(mDNA)-1))
   if colormode == 'RGB':
      color_red = random.randint(0,255)
      color_green = random.randint(0,255)
      color_blue = random.randint(0,255)
      color = (color_red, color_blue, color_green)
   else: #colormode == 'L':
      color = random.randint(0,255)
   mDNA[index][0] = color

def change_color(mDNA):
   """
   Change Color
   This takes a chromosome and shifts its color values independently by a
    random (small) difference.
   The resulting color is very close to the original color (as opposed to
    'New Color').
   """
   index = random.randint(0,max(0,len(mDNA)-1))
   if colormode == 'RGB':
      color_red = random.randint(-25,25)
      color_green = random.randint(-25,25)
      color_blue = random.randint(-25,25)
      color = mDNA[index][0]
      newcolor = (color[0]+color_red,color[1]+color_green,color[2]+color_blue)
   else: #colormode == 'L':
      color_diff = random.randint(-25,25)
      color = mDNA[index][0]
      newcolor = color+color_diff
   mDNA[index][0] = newcolor

def switch_colors(mDNA):
   """
   Switch Colors
   This picks two chromosomes at random and switches their colors.
   """
   index1 = random.randint(0,max(0,len(mDNA)-1))
   index2 = random.randint(0,max(0,len(mDNA)-1))
   temp = mDNA[index1][0]
   mDNA[index1][0] = mDNA[index2][0]
   mDNA[index2][0] = temp

def shuffle_colors(mDNA):
   """
   Shuffle Colors
   This takes the colors over every chromosome and 
    randomly shuffles all of them.
   Each chromosome gets a color that a chromosome had before
    (with each having equal probability).
   """
   mDNA

def mutate_opacity(mDNA):
   """
   Opacity Actions
   These actions only affect the opacity of the chromosomes.
   """
   seed = random.randint(0,2)
   if seed == 0:
      new_opacity(mDNA)
   elif seed == 1:
      change_opacity(mDNA)
   else: #seed == 2:
      switch_opacities(mDNA)
   #else: #seed == 3: # depricated
   #   shuffle_opacities(mDNA)

def new_opacity(mDNA):
   """
   New Opacity
   This takes a chromosome and assigns it a completely random new opacity
    (regardless of the previous opacity).
   """
   index = random.randint(0,max(0,len(mDNA)-1))
   opacity = random.randint(0,255)
   mDNA[index][1] = opacity

def change_opacity(mDNA):
   """
   Change Opacity
   This takes a chromosome and shifts its opacity value 
    by a random (small) difference.
   The resulting color is very close to the original color 
    (as opposed to 'New Opacity').
   """
   index = random.randint(0,max(0,len(mDNA)-1))
   opacity = random.randint(-25,25)
   mDNA[index][1] = opacity + mDNA[index][1]

def switch_opacities(mDNA):
   """
   Switch Opacities
   This picks two chromosomes at random and switches their colors.
   """
   index1 = random.randint(0,max(0,len(mDNA)-1))
   index2 = random.randint(0,max(0,len(mDNA)-1))
   temp = mDNA[index1][1]
   mDNA[index1][1] = mDNA[index2][1]
   mDNA[index2][1] = temp

def shuffle_opacities(mDNA):
   """
   Shuffle Opacities
   This takes the opacity over every chromosome and 
    randomly shuffles all of them.
   Each chromosome gets an opacity that a chromosome had before 
    (with each having equal probability).
   """
   mDNA   

