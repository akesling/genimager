import Image, ImageChops
import sys
ImageChops.difference(Image.open(sys.argv[1]), Image.open(sys.argv[2])).show()
#ImageChops.invert(Image.open(sys.argv[1])).show()
