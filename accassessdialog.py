# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AccAssessDialog
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

from PyQt4 import QtCore, QtGui
from ui_accassess import Ui_AccAssess
from qgis.core import QgsMapLayerRegistry, QgsMapLayer

class AccAssessDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_AccAssess()
        self.ui.setupUi(self)
        
    def initLayerCombobox(self,combobox, default):
         combobox.clear()
         reg = QgsMapLayerRegistry.instance()
         for ( key, layer ) in reg.mapLayers().iteritems():
             
             if layer.type() == QgsMapLayer.RasterLayer: #This doesn't work in QGIS2.0. Can I do without?: and ( layer.usesProvider() and layer.providerKey() == 'gdal' ):
                 combobox.addItem( layer.name(), key )
         
         idx = combobox.findData( default )
         if idx != -1:
             combobox.setCurrentIndex( idx ) 
             
    def layerFromComboBox(self, combobox):
        layerID = str( combobox.itemData(combobox.currentIndex()) )
        return QgsMapLayerRegistry.instance().mapLayer( layerID )