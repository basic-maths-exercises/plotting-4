import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==500, "The number of plotted data points is incorrect" )
        delx = 20 / 499
        for i in range( len(this_x) ) :
            xval = -10+i*delx
            yval = -2*xval*xval + 4*xval - 8
            self.assertTrue( np.abs(-10+i*delx-this_x[i])<1e-7, "One or more of the x-coordinates of your points is incorrect" )
            self.assertTrue( np.abs(yval-this_y[i])<1e-7, "One or more of the y-coordinates of your points is incorrect" )
