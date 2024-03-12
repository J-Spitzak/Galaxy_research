# Download an example FITS file, create a 2D cutout, and save it to a
# new FITS file, including the updated cutout WCS.
from astropy.io import fits
from astropy.nddata import Cutout2D
from astropy.utils.data import download_file
from astropy.wcs import WCS
from sys import argv

# Download the image
filename = str(argv[1]) 
new_position = (float(input("x co-ordonite: ")),float(input("y-coordonite: ")))
new_size = int(input("diameter: "))

# Load the image and the WCS
hdu = fits.open(filename)[0]
new_wcs = WCS(hdu.header)

# Make the cutout, including the WCS
cutout = Cutout2D(hdu.data, position=new_position, size=new_size, wcs=new_wcs)

 # Put the cutout image in the FITS HDU
hdu.data = cutout.data

# Update the FITS header with the cutout WCS
hdu.header.update(cutout.wcs.to_header())

# Write the cutout to a new FITS file
cutout_filename = (str(input("galaxy name: ")) + "-" + str(input("band letter: ")) "-corrected.fits")
hdu.writeto(cutout_filename, overwrite=True)
