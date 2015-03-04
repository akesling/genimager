# Introduction #

## Text-based Output ##
Example Formatting for xml-based output:

Note, the ` <fill> ` options are for color and black and white.  You only need to set the ` <grayscale> ` tag or the ` <red> `, ` <green> `, and ` <blue> ` tags, not both.
```
<?xml version="1.0" encoding="ISO-8859-1"?>
<simulation xmlns="http://code.google.com/p/genimager/wiki/OutputSpecifications">

<image>
  <width>Width of Image</width>
  <height>Height of Image</height>
  <background_color>Background Color</background_color>
  <color_mode>Color Mode</color_mode>
</image>

<genetic_history>
  <genome generation="Your Generation Number Here">
    <chromosome index="This Chromosome's Index">
      <fill>
        <red>Red Value From 0 to 255</red>
        <green>Green Value From 0 to 255</green>
        <blue>Blue Value From 0 to 255</blue>
        <grayscale>Gray Value from 0 to 255</grayscale>
        <opacity>Opacity Value From 0 to 255</opacity>
      </fill>
      <shape>
         <phenotype>polygon<phenotype>
         <point index="This point's index">
           <x>X Position</x>
           <y>Y Position</y>
         </point>
         ...
      </shape>
    </chromosome>
    ...
  </genome>
  ...
</genetic_history>
 
<mutation_history>
  <mutation generation="generation number">
    <success>True or False</success>
    <type>Mutation Type</type>
    <mutation_range>Probability Range for this type of mutation</mutation_range>
    <global_range>Probability range for all mutations</global_range>
    <!-- There is always 1 or 2 chromosome_index's -->
    <chromosome_index>Index Number</chromosome_index>
    <!-- There can be 0, 1 or 2 point_index's -->
    <point_index>Index Number</point_index>
    <!-- For anything else, tags are only included if that aspect it changed -->
    <new_fill>
      <new_red>Red Value From 0 to 255</new_red>
      <new_green>Green Value From 0 to 255</new_green>
      <new_blue>Blue Value From 0 to 255</new_blue>
      <new_grayscale>Gray Value from 0 to 255</new_grayscale>
      <new_opacity>Opacity Value From 0 to 255</new_opacity>
    </new_fill>
    <!-- If the fill was adjusted by difference, include that and not the new values -->
    <fill_difference>
      <fill_difference_sigma>sigma value</fill_difference_sigma>
      <red_difference>red difference value</red_difference>
      <green_difference>red difference value</green_difference>
      <blue_difference>red difference value</blue_difference>
      <grayscale_difference>red difference value</grayscale_difference>
      <opacity_difference>red difference value</opacity_difference>
    </fill_difference>
    <new_point>
      <new_x>Point Value</new_x>
      <new_y>Point Value</new_y>
    </new_point>
    <point_difference>
      <point_difference_sigma>sigma value</point_difference_sigma>
      <radius>radius the point moved</radius>
      <angle>angle for the direction the point moved</angle>
    </point_difference>
    <!-- This new_shape should only be used when inserting a new chromosome -->
    <new_shape>
      <phenotype>polygon</phenotype>
      <!-- there are exactly three points for a new polygon -->
      <point>
        <x>Point Value</x>
        <y>Point Value</y>
      </point>
      ...
    </new_shape>
  </mutation>
  ...
</mutation_history>

</simulation>
```

This example uses polygons as the entity that defines the image, but one could just as easily have ` <line> `, ` <rectangle> `, ` <ellipse> `, or any other geometric shape (JUST KEEP THE NAMING CONVENTION STANDARD).  The contents of ` <shape> ` would have to be changed accordingly.

For now, only ` polygon ` is supposed so nothing else needs to go in ` <phenotype> ` yet.

## Mutation History Notes ##
there can be at most two chromosome indexes and point indexes.  There has to be at least one chromosome index.  Other than that