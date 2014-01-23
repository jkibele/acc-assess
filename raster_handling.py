from osgeo import gdal, ogr
from osgeo.gdalconst import *
from error_matrix import *

class RasterDS(object):
    """
    Well be getting raster layers as Qgis raster layers but we need to do gdal
    stuff with them. This object will let us do that and let us make our own
    methods.
    """
    def __init__(self, rlayer, overwrite=False):
        self.rlayer = rlayer
        self.file_path = str( rlayer.publicSource() )
        self.gdal_ds = self.__open_gdal_ds()
        
    def __open_gdal_ds(self):
        """return a gdal datasource object"""
        # register all of the GDAL drivers
        gdal.AllRegister()
    
        # open the image
        img = gdal.Open(self.file_path, GA_ReadOnly)
        if img is None:
            print 'Could not open %s' % self.file_path
            return None
        else:
            return img
            
    @property
    def band_array(self):
        """Take a raster datasource and return a band array. Each band is read
        as an array and becomes one element of the band array."""
        img = self.gdal_ds
        for band in range(1,img.RasterCount + 1):
            barr = img.GetRasterBand(band).ReadAsArray()
            if band==1:
                bandarr = np.array([barr])
            else:
                bandarr = np.append(bandarr,[barr],axis=0)
        return bandarr
    
