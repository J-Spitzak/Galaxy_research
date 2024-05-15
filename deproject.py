import astropy.io
from astropy.io import fits
from photutils.isophote import Ellipse, EllipseGeometry
from photutils.aperture import EllipticalAperture
import matplotlib.pyplot as plt
import sys

fitsImage = fits.open(input("input image: "))

data = fitsImage[0].data

ellipse = Ellipse(data, None)
isolist = ellipse.fit_image()
print(isolist.pa)

if sys.argv[1] = "c":
    print("Create custom fit:")
    plt.imshow(data, origin='lower')

    x = float(input("center x: "))
    y = float(input("center y: "))
    
    x_minor = float(input("minor axis x coordonite: "))
    y_minor = float(input("minor axis y coordonite: "))

    x_major = float(input("major axis x coordonite: ")) 
    y_major = float(input("major axis y coordonite: "))  
    
    Major = math.sqrt( (math.abs( x_major - x ))**2 + (math.abs( y_major - y ))**2 ) #gives length of one of the halves of the major axis
    Minor = math.sqrt( (math.abs( x_minor - x ))**2 + (math.abs( y_minor - y ))**2 ) #gives length of one of the halves of the minor axis
    Ellipticity = (Major - Minor) / Major #Ellipticity according to here: https://phys.libretexts.org/Bookshelves/Astronomy__Cosmology/Celestial_Mechanics_(Tatum)/02%3A_Conic_Sections/2.02%3A_The_Ellipse 

    geometry = EllipseGeometry(x0=x, y0=y, sma=Major, eps=Ellipticity,pa=20.0 * np.pi / 180.0)



