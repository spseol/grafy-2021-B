import pylab as pl
import scipy.interpolate as interpol


x = "0 0.3 0.5 0.8 1  2  3".split()
y = "0 0.1 0.5 1   3 10 30".split()
x = tuple(map(float, x))
y = tuple(map(float, y))


pl.plot(x, y, "o")


# ( linear , nearest ,  zero ,  slinear ,  quadratic,  cubic )
funkce = interpol.interp1d(x, y, kind="nearest")

funkce = interpol.UnivariateSpline(x, y)

newX = pl.linspace(min(x), max(x), 300)
newY = funkce(newX)

pl.plot(newX, newY, ":")

pl.show()
