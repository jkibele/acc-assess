##Accuracy Assessment


####Accuracy Assessment plugin for QGIS 2.0

[![DOI](https://zenodo.org/badge/5590/jkibele/acc-assess.png)](http://dx.doi.org/10.5281/zenodo.11318)

by Jared Kibele 

Graduate Student at [Leigh Marine Lab](http://www.marine.auckland.ac.nz/en/about/our-institute/leigh-marine-laboratory.html), [University of Auckland](https://www.auckland.ac.nz/en.html)

<jkibele@gmail.com>

This plugin calculates an error matrix from two raster datasets and 
outputs a CSV file that can be loaded into a spreadsheet (LibreOffice 
Calc, or MicroSloth Excel). To use it, open your raster layers in 
QGis, launch the plugin, select the layer you want to use as the 
reference layer, select your comparison layer, and select an output 
file with a .csv extension. Click 'OK' then open your .csv file with a 
spreadsheet. You should see something like this:


    LayerName1 (ref) vs. LayerName2                     
                1   2   3   4   Totals  Accuracy
            1   618 0   0   3   621     100
            2   0   570 2   0   572     100
            3   0   0   313 2   315     99
            4   0   0   1   383 384     100
    Totals      618 570 316 388 1892    
    Accuracy    100 100 99  99          100
                        
    Quantity Disagreement   5                   
    Allocation Disagreement 3                   


The classes in this example are integers 1, 2, 3, 4. The reference 
layer is laid out in columns (so the reference class labels are 
headers in a row) and the comparison map data is laid out in rows (so 
the comparison class labels are in the first column). User's accuracy 
is in the 'Accuracy' column and producer's accuracy is in the 
'Accuracy' row (see Congalton 1991 in references.txt). For a 
description of Quantity Disagreement and Allocation Disagreement, see 
Pointius and Millones 2011 (references.txt)

Current Limitations: This plugin assumes that raster values of 0 are 
unclassified so you can't use 0 as a class value. The plugin also 
assumes that you're providing it with two rasters that have the same 
pixel size and dimensions. I haven't tested it yet with different 
sized rasters. If it doesn't crash with different sized rasters, it 
will at least give you useless results. I intend to address that in 
future versions. 

error_matrix.py can do other calculations that are currently not 
implemented in the GUI. error_matrix.py also has a bunch of 
explanitory comments that I won't include here. At some point I'd like 
to get the Sphinx documentation working with those comments but that 
will have to wait for a future version. error_matrix.py also has a 
bunch of doc tests. If you want to check that the code is working on 
your machine, go to the directory that contains error_matrix.py with 
the command line and type: "python error_matrix.py" and hit return. If 
you get output, please email it to me. If you just get another command 
prompt, that means the tests all passed.

This plugin was built with the "Plugin Builder" plugin by GeoApt LLC - 
geoapt.com. Thanks GeoApt.

-Jared
