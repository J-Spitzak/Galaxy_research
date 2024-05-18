import astropy.io
from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from photutils.isophote import Ellipse, EllipseGeometry
from photutils.aperture import EllipticalAperture
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import math
import sys
import warnings
warnings.filterwarnings("error")

inputFile = sys.argv[1]
bandLetter = input("band: ")

fitsImage = fits.open(inputFile)

data = fitsImage[0].data

try:
    
    ellipse = Ellipse(data, None)
    isolist = ellipse.fit_image()
    print(isolist.pa)

except RuntimeWarning:
    print("Creating custom fit:")

    plt.imshow(data,norm=LogNorm(), origin='lower')
    plt.show()


    x = float(input("center x: "))
    y = float(input("center y: "))
    
    x_minor = float(input("minor axis x coordonite: "))
    y_minor = float(input("minor axis y coordonite: "))

    x_major = float(input("major axis x coordonite: ")) 
    y_major = float(input("major axis y coordonite: "))  
    

    Major = math.sqrt( (abs( x_major - x ))**2 + (abs( y_major - y ))**2 ) #gives length of one of the halves of the major axis
    Minor = math.sqrt( (abs( x_minor - x ))**2 + (abs( y_minor - y ))**2 ) #gives length of one of the halves of the minor axis
    Ellipticity = (Major - Minor) / Major #Ellipticity according to here: https://phys.libretexts.org/Bookshelves/Astronomy__Cosmology/Celestial_Mechanics_(Tatum)/02%3A_Conic_Sections/2.02%3A_The_Ellipse 
    
    Angle = math.asin( abs(y_major - y) / Major )
    
    if x_major - x < 0:
        Angle = math.pi - Angle
    geometry = EllipseGeometry(x0=x, y0=y, sma=Major, eps=Ellipticity,pa=Angle)


    aper = EllipticalAperture((geometry.x0, geometry.y0), geometry.sma, geometry.sma * (1 - geometry.eps),geometry.pa)
    aper.plot(color='white')

    cutout = Cutout2D(data.data, position=(x,y), size=Major, wcs=WCS(fitsImage[0].header))
   
    hdu = fits.open(inputFile)[0]
    hdu.data = cutout.data
    hdu.header.update(cutout.wcs.to_header())
    cutout_filename = (inputFile + "_" + str(bandLetter) + "_corrected")
    hdu.writeto(cutout_filename, overwrite=True)

    newImage = fits.open(cutout_filename)
    newData = newImage[0].data

    plt.imshow(newData,norm=LogNorm(), origin='lower')
    plt.show()
    
