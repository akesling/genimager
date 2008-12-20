#!/usr/bin/python
#  XML Module
#  This uses xml.dom.minidom to create 
#   an XML record of a simulation

## Create XML Document ##
def create_xml_document():
   """
   Create XML Document
   Returns an xml document from of xml.dom.minidom
   With the root element:simulation and the child
   elements: genetic_history and mutation_history
   """
   # create our minidom document
   from xml.dom.minidom import getDOMImplementation
   doc = getDOMImplementation().createDocument(None, "simulation", None)
   # grab the root element (this does nothing to the doc, it just gives us a name for the root element)
   simulation = doc.documentElement
   # Create child elements
   genetic_history = doc.createElement('genetic_history')
   mutation_history = doc.createElement('mutation_history')
   # Attach the child elements to the root element
   simulation.appendChild(genetic_history)
   simulation.appendChild(mutation_history)
   # clean up by explicitly garbage-collecting the nodes
   simulation.unlink()
   genetic_history.unlink()
   mutation_history.unlink()
   # now return the doc to the user
   return doc
   
## Add Genome ##
def add_genome(doc,genome,generation=None):
   """
   Add Genome
   This take an XML document created by this module
   and adds a genome you gave to it.
   It optionally takes a generation parameter
   that gets stored as the genomes attribute.
   The genome must be iterable
   """
   # Right now we only do polygons, so set the phenotype
   phenotype = 'polygon'
   # grab the root element
   simulation = doc.documentElement
   # grab the genetic_history element
   genetic_history = simulation.getElementsByTagName('genetic_history')
   # create the element for the genome
   genome_elem = doc.createElement('genome')
   # attach genome to the genetic_history
   genetic_history.appendChild(genome_elem)
   # attach generation attribute if given
   if generation != None:
      generation_attrib = doc.createAttribute('generation')
      genome_elem.setAttributeNode(generation_attrib)
      genome_elem.setAttribute('generation',str(generation))
      generation_attrib.unlink()
   # add chromosomes, genome must be iterable
   for chrom_index in xrange(len(genome)):
      chromosome = genome[chrom_index]
      chromosome_elem = doc.createElement('chromosome')
      genome_elem.appendChild(chromosome_elem)
      chrom_index_attrib = doc.createAttribute('index')
      chromosome_elem.setAttributeNode(chrom_index_attrib)
      chromosome_elem.setAttribute('index',str(chrom_index))
      # pull off the fill
      fill_elem = doc.createElement('fill')
      chromosome_elem.appendChild(fill_elem)
      fill = chromosome[0]
      # check for grayscale or color
      if len(fill) == 4: # R,G,B,A ; color
         # red
         red_elem = doc.createElement('red')
	 fill_elem.appendChild(red_elem)
	 red_text = doc.createTextNode(str(fill[0]))
	 red_elem.appendChild(red_text)
	 # green
         green_elem = doc.createElement('green')
	 fill_elem.appendChild(green_elem)
	 green_text = doc.createTextNode(str(fill[1]))
	 green_elem.appendChild(green_text)
	 # blue
         blue_elem = doc.createElement('blue')
	 fill_elem.appendChild(blue_elem)
	 blue_text = doc.createTextNode(str(fill[2]))
	 blue_elem.appendChild(blue_text)
	 # opacity
         opacity_elem = doc.createElement('opacity')
	 fill_elem.appendChild(opacity_elem)
	 opacity_text = doc.createTextNode(str(fill[3]))
	 opacity_elem.appendChild(opacity_text)
      else: # L, A ; grayscale
	 # grayscale
         grayscale_elem = doc.createElement('grayscale')
	 fill_elem.appendChild(grayscale_elem)
	 grayscale_text = doc.createTextNode(str(fill[0]))
	 grayscale_elem.appendChild(grayscale_text)
	 # opacity
         opacity_elem = doc.createElement('opacity')
	 fill_elem.appendChild(opacity_elem)
	 opacity_text = doc.createTextNode(str(fill[1]))
	 opacity_elem.appendChild(opacity_text)
      # now add points
      shape_elem = doc.createElement('shape')
      chromosome_elem.appendChild(shape_elem)
      # define the phenotype
      phenotype_elem = doc.createElement('phenotype')
      shape_elem.appendChild(phenotype_elem)
      phenotype_text = doc.createTextNode(phenotype)
      phenotype_elem.appendChild(phenotype_text)
      # grab points and iterate over them
      points = chromosome[1]
      for index in xrange(len(points)):
         point_elem = doc.createElement('point')
	 shape_elem.appendChild(point_elem)
	 index_attrib = doc.createAttribute('index')
	 point_elem.setAttributeNode(index_attrib)
	 point_elem.setAttribute('index',str(index))
	 # x coordinate
	 x_value = points[index][0]
	 x_elem = doc.createElement('x')
	 point_elem.appendChild(x_elem)
	 x_text = doc.createTextNode(str(x_value))
	 x_elem.appendChild(x_text)
	 # y coordinate
	 y_value = points[index][1]
	 y_elem = doc.createElement('y')
	 point_elem.appendChild(y_elem)
	 y_text = doc.createTextNode(str(y_value))
	 y_elem.appendChild(y_text)
      # now just garbage cleanup and go home
      simulation.unlink()
      genetic_history.unlink()
      genome_elem.unlink()
      chromosome_elem.unlink()
      chrom_index_attrib.unlink()
      fill_elem.unlink()
      if len(fill) == 4: # unlink colors
	 red_elem.unlink()
	 red_text.unlink()
	 blue_elem.unlink()
	 blue_text.unlink()
	 green_elem.unlink()
	 green_text.unlink()
      else: #unlink grayscale
         grayscale_elem.unlink()
	 grayscale_text.unlink()
      opacity_elem.unlink()
      opacity_text.unlink()
      shape_elem.unlink()
      phenotype_elem.unlink()
      phenotype_text.unlink()
      point_elem.unlink()
      index_attrib.unlink()
      x_elem.unlink()
      x_text.unlink()
      y_elem.unlink()
      y_text.unlink()
      # the doc was modified in place, return nothing