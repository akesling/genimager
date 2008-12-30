#!/usr/bin/python
# genimagef.py - function-based genetic imager
# Creates a genome based on a bunch of chromosomes (shapes)
# that mutates to look like a base image
import Image, ImageDraw, ImageChops, ImageStat
import random
random.seed()

def genimage(image_path, archive_dir='.', max_generations=None, \
   color_mode='RGB', save_interval=1, output_type=None, phenotype="Poly"):
   """
   Genetic Imager
   This takes an image, as well as operational parameters
   and evolves a genome to the environment of that image.
   The 'fitness function' is merely a measure of how close
   the genome is to its environment.

   Genomes come in different shapes: polygons, ellipses,
   rectangles, circles, and triangles.
   *currently only supports polygons
   
   Parameters:
   image_path ; path to the image to use
   archive_dir = '.' ; path to directory for output files
   max_generations = None; maximum number of generations
   color_mode = 'RGB'; 'RGB' color, 'L' black & white
   save_interval = 1; How often to save genome
   output_type = None; output filetype 'GEN','XML', or None
   """
   # this is filename for any output
   filename = image_path
   filename = filename[filename.rfind('/')+1:]	#strip the path
   filename = filename[:filename.find('.')]	#strip the file extension
   if color_mode == 'RGB':
      background_color = (0,0,0)
   else: #color_mode == 'L'
      background_color = 0
   genome = []	# the genome - this is what mutates
   base_image = Image.open(image_path).convert(color_mode)
   imagewidth, imageheight = base_image.size
   import mutate, fitness
   # Set the globals
   mutate.imagewidth = imagewidth
   fitness.imagewidth = imagewidth
   mutate.imageheight = imageheight
   fitness.imageheight = imageheight
   mutate.color_mode = color_mode
   fitness.color_mode = color_mode
   fitness.background_color = background_color
   fitness.base_image = base_image
   fitness.phenotype = phenotype
   mutate.phenotype = phenotype
   # 
   genome_image = fitness.draw_genome(genome) # Image from genome
   difference = fitness.image_difference(genome_image)
   generation_counter = 0
   success_counter = 0
   while generation_counter <= max_generations:
      generation_counter = generation_counter + 1
      mutated_genome = mutate.mutate(genome) #mutate the genome
      mutated_image = fitness.draw_genome(mutated_genome) # Image from mutated genome
      mutation_difference = fitness.image_difference(mutated_image) # difference of mutated genome to base image
      if (mutation_difference == difference): # if there is no appreciable difference, keep it
         genome = mutated_genome
         genome_image = mutated_image
         difference = mutation_difference
      elif (mutation_difference < difference):
         success_counter = success_counter + 1
         genome = mutated_genome
         genome_image = mutated_image
         difference = mutation_difference
         print 'level up! counter:',generation_counter,'diff:',difference,'success_counter:',success_counter
         print genome
         if save_interval != None and success_counter % save_interval == 0:
            genome_image.save(archive_dir + '/' + filename + '_' + str(generation_counter)+'.jpg','JPEG')
