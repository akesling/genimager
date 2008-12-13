import copy, random

def mutate(DNA):
   """
   Mutate Function
   This mutation function is made up of four basic sections, and each of these four sections has four actions.
   Every action has an equal weight except for special cases (where noted).
   Special Case: If the genome has no chomosomes, then it forces the mutation 'Insert Chomosome'.
   """
   mDNA = copy.deepcopy(DNA) # make a copy of the DNA to mutate
   seed = random.randint(0,3)
   if seed == 0:
      return mutate_chromosome(mDNA)
   elif seed == 1:
      return mutate_point(mDNA)
   elif seed == 2:
      return mutate_color(mDNA)
   else: #seed ==3:
      return mutate_opacity(mDNA)

def mutate_chromosome(mDNA):
   """
   Chomosome Mutations
   These are actions that apply to chromosomes within the genome.
   Special Case: If the genome has 100 chromosomes, it will not 'insert chromosome'. This is effectively the maximum number of chromosomes.
   """
   seed = random.randint(0,5)
   if seed == 0:
      return insert_chromosome(mDNA)
   elif seed == 1:
      return remove_chromosome(mDNA)
   elif seed == 2:
      return switch_chromosomes(mDNA)
   elif seed == 3:
      return shuffle_chromosomes(mDNA)
   elif seed == 4:
      return increment_chromosome(mDNA)
   else: #seed == 5:
      return decrement_chromosome(mDNA)

def insert_chromosome(mDNA):
   """
   Insert Chromosome
   Inserts a chromosome with no points at a random index. This chromosome has a random color and opacity.
   """
   return mDNA

def remove_chromosome(mDNA):
   """
   Remove Chromosome
   Removes a chromosome from a randomly chosen index.
   """
   return mDNA

def switch_chromosomes(mDNA):
   """
   Switch Chromosomes
   Choses two random chromosomes and switches them in place.
   """
   return mDNA

def shuffle_chromosomes(mDNA):
   """
   Shuffle Chromosomes
   Shuffle the order of all chromosomes.
   """
   return mDNA

def increment_chromosome(mDNA):
   """
   Increment Chromosome
   Choose a chromosome at random and move it up the list.
   """
   return mDNA

def decrement_chromosome(mDNA):
   """
   Decrement Chromosome
   Choose a chromosome at random and move it down the list.
   """
   return mDNA

def mutate_point(mDNA):
   """
   Point Mutation
   These actions affect the size, shape, and location of the chromosomes' phenotype.
   The phenotype may be polygons, triangles, ellipses, circles, rectangles, diamonds, etc...
   """
   seed = random.randint(0,7)
   if seed == 0:
      return insert_point(mDNA)
   elif seed == 1:
      return remove_point(mDNA)
   elif seed == 2:
      return switch_points(mDNA)
   elif seed == 3:
      return shuffle_points(mDNA)
   elif seed == 4:
      return move_point(mDNA)
   elif seed == 5:
      return shift_point(mDNA)
   elif seed == 6:
      return increment_point(mDNA)
   else: #seed == 7:
      return decrement_point(mDNA)

def insert_point(mDNA):
   """
   Insert Point
   This randomly inserts a point. For polygons, this inserts a point randomly into its list of points.
   For ellipses and other phenotypes with a fixed number of points, this overwrites a randomly chosen with a new randomly placed point.
   """
   return mDNA

def remove_point(mDNA):
   """
   Remove Point
   This randomly removes a point. For polygons this removes a randomly selected point in the list of points.
   For ellipses and other phenotypes with a fixed number of points, this overwrites a randomly chosen point with a new randomly placed point.
   """
   return mDNA

def switch_points(mDNA):
   """
   Switch Points
   Chooses two points and randomly switches them in place.
   """
   return mDNA

def shuffle_points(mDNA):
   """
   Shuffle Points
   Shuffle the order of all points in place.
   """
   return mDNA

def move_point(mDNA):
   """
   Move Point
   Chooses a point at random and moves it to a randomly chosen location. This can be anywhere on the image (or even slightly off of it).
   """
   return mDNA

def shift_point(mDNA):
   """
   Shift Point
   Chooses a point at random and moves it by a randomly selected amount.
   This amount is in general smaller than the image to make this a much more gradual move than Move Point.
   """
   return mDNA

def increment_point(mDNA):
   """
   Increment Point
   Choose a point at random and move it up the list.
   """
   return mDNA

def decrement_point(mDNA):
   """
   Decrement point
   Choose a point at random and move it down the list.
   """
   return mDNA

def mutate_color(mDNA):
   """
   Color Mutations
   These actions only affect the color of the chromosomes.
   """
   seed = random.randint(0,5)
   if seed == 0:
      return new_color(mDNA)
   elif seed == 1:
      return change_color(mDNA)
   elif seed == 2:
      return switch_colors(mDNA)
   else: #seed == 3:
      return shuffle_colors(mDNA)

def new_color(mDNA):
   """
   New Color
   This takes a chromosome and assigns it a completely random new color(regardless of the previous color).
   """
   return mDNA

def change_color(mDNA):
   """
   Change Color
   This takes a chromosome and shifts its color values independently by a random (small) difference.
   The resulting color is very close to the original color (as opposed to 'New Color').
   """
   return mDNA

def switch_colors(mDNA):
   """
   Switch Colors
   This picks two chromosomes at random and switches their colors.
   """
   return mDNA

def shuffle_colors(mDNA):
   """
   Shuffle Colors
   This takes the colors over every chromosome and randomly shuffles all of them.
   Each chromosome gets a color that a chromosome had before (with each having equal probability).
   """
   return mDNA

def mutate_opacity(mDNA):
   """
   Opacity Actions
   These actions only affect the opacity of the chromosomes.
   """
   seed = random.randint(0,3)
   if seed == 0:
      return new_opacity(mDNA)
   elif seed == 1:
      return change_opacity(mDNA)
   elif seed == 2:
      return switch_opacities(mDNA)
   else: #seed == 3:
      return shuffle_opacities(mDNA)

def new_opacity(mDNA):
   """
   New Opacity
   This takes a chromosome and assigns it a completely random new opacity(regardless of the previous opacity).
   """
   return mDNA

def change_opacity(mDNA):
   """
   Change Opacity
   This takes a chromosome and shifts its opacity value by a random (small) difference.
   The resulting color is very close to the original color (as opposed to 'New Opacity').
   """
   return mDNA

def switch_opacities(mDNA):
   """
   Switch Opacities
   This picks two chromosomes at random and switches their colors.
   """
   return mDNA

def shuffle_opacities(mDNA):
   """
   Shuffle Opacities
   This takes the opacity over every chromosome and randomly shuffles all of them.
   Each chromosome gets an opacity that a chromosome had before (with each having equal probability).
   """
   return mDNA   

