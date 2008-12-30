#!/usr/bin/python
#  Fitness Function
#    EXCLUSIVELY POLYGONS
#  This is how the program decides if a genome is fit
import Image, ImageDraw, ImageChops, ImageStat
global background_color, color_mode, imagewidth, imageheight, base_image

def draw_genome(genome):
   genome_image = Image.new(color_mode,(imagewidth,imageheight),background_color)
   # Draw polygons from a list of points
   for polygon in genome:
      color, opacity, points = polygon
      color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
      polygon_mask = Image.new('L',(imagewidth,imageheight), 0)
      if len(points) >= 3:
         ImageDraw.Draw(polygon_mask).polygon(points, fill=opacity)
      elif len(points) == 2:
         ImageDraw.Draw(polygon_mask).line(points, fill=opacity)
      else: #len(points) == 1:
         ImageDraw.Draw(polygon_mask).point(points, fill=opacity)
      genome_image = Image.composite(color_mask,genome_image,polygon_mask)
   return genome_image

def image_difference(genome_image):
   """
   Image Difference
   takes two images and returns the differece
   calculated per pixel by taking the sum of the sqaured difference of each color
   and summing all of these over the whole image
   """
   difference_image = ImageChops.difference(genome_image, base_image) 
   difference_statistics = ImageStat.Stat(difference_image) # statistics for difference_image
   difference_value = sum(difference_statistics.sum2) #returns a list of each color sum**2
   return difference_value
