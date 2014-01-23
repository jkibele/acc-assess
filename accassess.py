# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AccAssess
                                 A QGIS plugin
 Generate an error matrix and measures of mapping accuracy for raster and reference data.
                              -------------------
        begin                : 2014-01-23
        copyright            : (C) 2014 by Jared Kibele
        email                : jkibele@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from accassessdialog import AccAssessDialog
import os.path

#- Import custom code that actually does stuff. All the other imports
#- were written by Plugin Builder
from raster_handling import *
from error_matrix import *
import os

class AccAssess:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'accassess_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = AccAssessDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/accassess/icon.png"),
            u"Accuracy Assessment", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Accuracy Assessment", self.action)
        
        #- Hook the select button to a file dialog
        self.dlg.ui.outFileSelectButton.clicked.connect(self.showFileSelectDialog)
        
    def showFileSelectDialog(self):
        fname = QFileDialog.getSaveFileName(self.dlg, 'Save File', os.path.expanduser('~'))
        self.dlg.ui.outFileLineEdit.setText( fname )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Accuracy Assessment", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        #- populate the combo boxes with loaded layers
        self.dlg.initLayerCombobox( self.dlg.ui.referenceComboBox, 'key_of_default_layer' )
        self.dlg.initLayerCombobox( self.dlg.ui.comparisonComboBox, 'key_of_default_layer' )
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            #- this gets the layer label from the menu but that's not the key
            #-print self.dlg.ui.referenceComboBox.currentText()
            #- get the  layer
            ref_layer = self.dlg.layerFromComboBox( self.dlg.ui.referenceComboBox )
            comp_layer = self.dlg.layerFromComboBox( self.dlg.ui.comparisonComboBox )
            #- get some RasterDS objects (defined in raster_handling.py) so we can do
            #- gdal stuff.
            ref_ds = RasterDS(ref_layer)
            comp_ds = RasterDS(comp_layer)
            #- get 2d arrays from datasets. I'm currently assuming the extents are 
            #- the same. I'll need to change that later. I should also check the shape
            #- of the band array.
            ref_arr = ref_ds.band_array[0]
            comp_arr = comp_ds.band_array[0]
            #- I only want to compare non-zero values so I need the indexes of nonzeros
            idx = ref_arr.nonzero()
            #- get the error matrix
            em = error_matrix(ref_arr[idx],comp_arr[idx])  
            #- set the title
            em.title = "%s (ref) vs. %s" % (str(ref_layer.name()),str(comp_layer.name()))
            #- get the file name that's in the filename line edit (set in showFileSelectDialog)
            filename = str( self.dlg.ui.outFileLineEdit.text() )
            em.save_csv( filename )
