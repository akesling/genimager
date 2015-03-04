

# genimagef's Mutation Scheme #
This mutation function is made up of four basic sections, and each of these four sections has four actions. Every action has an equal weight except for special cases (where noted).

**Special Case:** If the genome has no chomosomes, then it forces the mutation 'Insert Chomosome'.

## Chomosome Actions ##
These are actions that apply to chromosomes within the genome.

**Special Case:** If the genome has 100 chromosomes, it will **not** 'insert chromosome'.  This is effectively the maximum number of chromosomes.
### Insert Chromosome ###
Inserts a chromosome with no points at a random index.  This chromosome has a random color and opacity.
### Remove Chromosome ###
Removes a chromosome from a randomly chosen index.
### Switch Chromosomes ###
Choses two random chromosomes and switches them in place.
### Shuffle Chromosomes ###
Shuffle the order of all chromosomes.
### Increment Chromosome ###
Choose a chromosome at random and move it up the list.
### Decrement Chromosome ###
Choose a chromosome at random and move it down the list.
## Point Actions ##
These actions affect the size, shape, and location of the chromosomes' phenotype.  The phenotype may be polygons, triangles, ellipses, circles, rectangles, diamonds, etc...
### Insert Point ###
This randomly inserts a point.  For polygons, this inserts a point randomly into its list of points.  For ellipses and other phenotypes with a fixed number of points, this overwrites a randomly chosen with a new randomly placed point.
### Remove Point ###
This randomly removes a point.  For polygons this removes a randomly selected point in the list of points.  For ellipses and other phenotypes with a fixed number of points, this overwrites a randomly chosen point with a new randomly placed point.
### Switch Points ###
Chooses two points and randomly switches them in place.
### Shuffle Points ###
Shuffle the order of all points in place.
### Move Point ###
Chooses a point at random and moves it to a randomly chosen location.  This can be anywhere on the image (or even slightly off of it).
### Shift Point ###
Chooses a point at random and moves it by a randomly selected amount.  This amount is in general smaller than the image to make this a much more gradual move than 'Move Point'.
### Increment Point ###
Choose a point at random and move it up the list.
### Decrement point ###
Choose a point at random and move it down the list.

## Color Actions ##
These actions only affect the color of the chromosomes.
### New Color ###
This takes a chromosome and assigns it a completely random new color(regardless of the previous color).
### Change Color ###
This takes a chromosome and shifts its color values independently by a random (small) difference.  The resulting color is very close to the original color (as opposed to 'New Color').
### Switch Colors ###
This picks two chromosomes at random and switches their colors.
### Shuffle Colors ###
This takes the colors over every chromosome and randomly shuffles all of them.  Each chromosome gets a color that a chromosome had before (with each having equal probability).

## Opacity Actions ##
These actions only affect the opacity of the chromosomes.
### New Opacity ###
This takes a chromosome and assigns it a completely random new opacity(regardless of the previous opacity).
### Change Opacity ###
This takes a chromosome and shifts its opacity value by a random (small) difference.  The resulting color is very close to the original color (as opposed to 'New Opacity').
### Switch Opacities ###
This picks two chromosomes at random and switches their colors.
### Shuffle Opacities ###
This takes the opacity over every chromosome and randomly shuffles all of them.  Each chromosome gets an opacity that a chromosome had before (with each having equal probability).