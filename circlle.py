import matplotlib.pyplot as plt
import numpy as np
import os
import pydicom
import scipy as sc
import scipy.misc
from scipy import stats
# image file example
filename = "Image5.dcm"
ds = pydicom.dcmread(filename)
dat = ds.pixel_array

# An image class with the relevant dicom tags
class Image:
    """Creates image objects with relevant dicom elements"""
    def __init__(self, x):
        self.pix = x.pixel_array
        self.modality = x.Modality
        self.test_date = ds.AcquisitionDate
        self.sensor_type = ds.DetectorType
        self.sensor_manufac = ds.DetectorManufacturerName
        self.sensor_bits = ds.BitsStored
        self.sensor_rows = ds.Rows
        self.sensor_columns = ds.Columns
        self.sensor_row_element_spacing = ds.DetectorElementSpacing[0]
        self.sensor_row_element_spacing = ds.DetectorElementSpacing[1]
        self.sensor_model = ds.DetectorManufacturerModelName

    def summary(self):
        print(self.modality)

# Creates a rectangular ROI of width = x pixels and length = y pixels
def rect_roi(a,x, y):

    """Creates a rectangular ROI of width = x pixels and height = y pixels

        Parameters:
        argument1 (numpy array): a numpy array
        argument1 (int): Number of pixels in horizontal (width)
        argument1 (int): Number of pixels in vertical direction (height)

        Returns:
        int:Returning value

       """
    h = a.shape[0]
    w = a.shape[1]

    return h*w

x4 = np.random.randint(10, size=(3,4))
# Pixel_stats is a fff
def pixel_stas(d):

    """Summary or Description of the Function

        Parameters:
        argument1 (int): Description of arg1

        Returns:
        int:Returning value

       """

    return np.mean(d)

print(rect_roi(dat, 1,2))