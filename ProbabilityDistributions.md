# Introduction: Distribution types #
The algorithms used two main types of distributions: uniform, weighted and normal.
## Uniform ##
This is the most simple of distributions.  This is currently how genimagef chooses what aspect to mutate and how to mutate that aspect.
## Weighted ##
This is similar to uniform, except certain events are given a wider or smaller range, making that even more or less probable, respectively.  This is currently how genimagec chooses what aspect to mutate: mutating individual chromosomes is weighted heavily over adding chromosomes whole.
## Normal ##
This is a normal distribution, where values closer to the mean are more probable than values farther away from the mean.  How fast the probability decreases as the value moves away from the mean is a function of it's standard deviation.
### Moving/Placing Points ###
One of the big issues in the mutation of polygons is that in general MANY mutations that you do to the shape of a polygon will make it worse than it already is.  To try to move up the success of mutations, we want to distribute the points such that smaller changes happen more often than larger changes. To do this we can use a Normal Distribution.

**Example Case:** poly\_imager's move\_point mutation

This move\_point mutation is calculated as a radius (distance from the original point to the new point) and an angle, theta (angle between the horizontal base of the image, and the line connecting the old and new points).  the range of theta is a full circle [0,2\*pi) and the radius is given by the normal distribution: gauss(0,sigma).  The mean is 0 (so the expected move is no move at all), and this allows it to move forward along the angle as well as backwards along the angle.

For future this can be changed to use only a half circle, theta:[0,pi), because the radius has positive and negative values.

The probability of moving a point is high close to the point and decreases as a function of distance from the point and sigma.  The two types of simulations for this are Static and Dynamic. Static simulations fix the sigma, and Dynamic simulations allow the simulation to vary sigma for the highest rate of success.