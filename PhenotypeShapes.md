

# Shapes #
Every chomosome (individual shape) is a list with three elements:
  * Color - a color to shade the shape with
  * Opacity - an opacity to shade the shape with
  * Points - a list of points which defines where the polygon goes on the image; the exception to this is where the list would only contain exactly one element (a tuple) then the 'points' is that tuple itself.  Additionally, anything with a fixed number of points is a tuple of tuples (e.g. triangles).

**Note:** Only polygons works currently.
## Polygons ##
This is the basic shape we started with.  A polygon which has 3 or more points.

` Poly: [(x,y),(x,y),(x,y),...]  `

## Polygon3 ##
This is the second type of polygons.  Polygons with 3 or more points are drawn normally, and polygons with 2 points are drawn as a line segment and polygons with 1 point are drawn as points.

` Poly3: [(x,y),...] `

## Triangles ##
These are similar to the first type of polygon, except these are limited to exactly 3 points.

` Trig: ((x,y),(x,y),(x,y)) `

## Circles ##
These are circles.  We identify them by a centerpoint and a radius.

` Circ: (x,y,r) `

Note: The Python Imaging Library only has an ellipse function, so we use that information to draw a 'squared' ellipse or a circle.

## Pieslices ##
These are pie (radial) slices of circles.  They are identified by a centerpoint, radius, start angle (theta<sub>0</sub>) and end angle (theta<sub>1</sub>).  These angles are measured clockwise from horizontal.

` PieS: (x,y,r,theta0,theta1) `

## Chord ##
These are like pie slices except instead of being radial, the arc's endpoints are connected with a straight line.  These are identified with the same elements as a pieslice.

` Chord: (x,y,r,theta0,theta1) `

## Ellipses ##
These are ellipses, they are identified by the opposite corners smallest orthogonal rectangle that contains them.  This means the orientation of the ellipse must be orthogonal (they can only be horizontal or vertical ellipses).

` Ellip: ((x,y),(x,y)) `

## Rotated Ellipses ##
These are ellipses that can be rotated.  They are identified by the orthogonal rectangle that contains them and the angle (theta) it is rotated counterclockwise.  They are rotated about their center.

` EllipR: ((theta,(x,y),(x,y)) `

## Rectangles ##
These are orthogonal rectangles.  They are identified like ellipses, with coordinates for opposite corners.

` Rect: ((x,y),(x,y)) `

## Rotated Rectangles ##
These are rotated rectangles, they are like rectangles exept there is an added angle, theta, that the rectangles are rotated about their center.

` RectR: (theta,(x,y),(x,y)) `

## Lines ##
These are just line segments given by a list of points. They are similar to polygons, excepting two differences: it does not fill in the interior and it does not connect the last point to the first point.  If the line only has one point, it is drawn as a point.

` Line: [(x,y),...] `

## Wide Line ##
These are the same as the line, except now the lines can be wider than one pixel.  It is a list with the width (in pixels) first followed by all of its points. Note: while the lines are drawn width pixels wide, points are still only drawn as one pixel.

` WLine: [width,(x,y),...] `

## Text ##
This draws text.  Should probably be combined with heavy upsampling (the genetic image is many times larger than the base image) so that the text is recognizeable.

` Text: ((x,y),"string",font) `

Where _font_ is an instance of ImageFont.

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages