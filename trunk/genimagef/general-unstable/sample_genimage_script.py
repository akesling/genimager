#!/usr/bin/python
# Sample script to test genetic imaging libraries
#
import genetic_imager

# specifies the path to the image
image_path = '/home/ajray/images/eyekey.jpg' 

# specifies the path to save the images to
archive_dir = '/home/ajray/images/eyekey/' 

# specifies the maximum number of generations
max_generations = 10000

# specifies color mode 'RGB' = color, 'L' = black & white
color_mode = 'L'

# specifies the interval to save images at, None means don't save images
save_interval = 10

# specifies the output format, None means no output
output_type = 'XML'

genetic_imager.genimage(image_path	= image_path, \
                        archive_dir	= archive_dir, \
                        max_generations	= max_generations, \
                        color_mode	= color_mode, \
                        save_interval	= save_interval, \
                        output_type	= output_type)
