#!/usr/bin/python
#  Fitness Function
#  This is how the program decides if a genome is fit
import Image, ImageDraw, ImageChops, ImageStat
from genetic_imager import ImageWidth, ImageHeight, background_color, color_mode

def draw_genome(genome):
  genome_image = Image.new(color_mode,(ImageWidth,ImageHeight),background_color)
  for polygon in genome:
    color, opacity, points = polygon
    if (len(points) >= 3):
      color_mask = Image.new(color_mode,(ImageWidth,ImageHeight), color)
      polygon_mask = Image.new(color_mode,(ImageWidth,ImageHeight), 0)
      ImageDraw.Draw(polygon_mask).polygon(points, fill=opacity) 
      genome_image = Image.composite(color_mask,genome_image,polygon_mask)
  return genome_image

def image_difference(genome_image, base_image):
   """
   Image Difference
   takes two images and returns the differece
   calculated per pixel by taking the sum of the sqaured difference of each color
   and summing all of these over the whole image
   """
   difference_image = ImageChops.difference(genome_image, base_image) 
   difference_statistics = ImageStat.Stat(difference_image) # statistics for difference_image
   difference_value = sum(difference_statistics.sum2) #stat.sum returns a list of each color sum**2
   return difference_value
