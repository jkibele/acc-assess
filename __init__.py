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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load AccAssess class from file AccAssess
    from accassess import AccAssess
    return AccAssess(iface)
