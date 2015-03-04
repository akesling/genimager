# Introduction #
## alexjray.ncsu ##
Top Stuff:
  * Downsampling - base image is smaller than it started (1/4?)
  * Upsampling - genome image is larger (4x?) than base (stays the same)

  * Figure out how to handle a max number of polygons
  * Handle a max number of points
  * Automatically re-seed itself for a continued simulation (DNA and counter)
  * Figure out how far points should go off the edge
  * ?Remove polygons that aren't rendered
  * Get alpha layer drawing/masking working
  * Find a useful way to display percent or ln(p) completed
  * Have it intelligently start with the background color (using trim mean of histograms?)
  * Output images intelligently (at intervals of count or difference or percentage)
  * ?Distribute simulation to VCL

**Meta-Evolution**
  * Figure out what distribution of mutations and probabilites gives fastest results
  * Have the above probabilities mutate (meta-evolution)
  * Have the mutations/generation mutate
  * Have a delicate-only mutation; moves very gradually (all polygons start at 0 opacity at background color)

Visualizer:
  * Program/function to visualize based on output DNA info
  * Represent progression in a single image by centering the final version in the middle and having a progression spiral (starting in the upper left) going clockwise inwards towards the final image.  This shows the substantial change in the image through the whole evolutionary process and gives the viewer a sense of how the final image came about.

Future:
**Make it a library/module that you can call with a little script in a dir w/ a base image**

## DONE! ##
  * ~~Take a 'archiving directory' and an 'image directory' by default~~
  * ~~**Standardize output format!**~~
  * ~~Mode settings: ('RGB','L') color and black & white~~
  * ~~Option = dont output images~~

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages