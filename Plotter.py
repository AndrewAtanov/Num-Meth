from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=4, height=7, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def plot(self, x, y):
        self.axes.plot(x, y, 'r')
        self.draw()

    def scatter(self, x, y):
        self.axes.scatter(x, y)
        self.draw()


class Plotter:
    def __init__(self, parent=None, solver=None, w=7, h=4, dpi=100):
        self.canvas = MyDynamicMplCanvas(parent=parent, width=w, height=h, dpi=dpi)
        self.solver = solver

    def plot(self, func, start, end):
        x = np.linspace(start, end, 100)

        if func == 'ro':
            self.canvas.plot(x, self.solver.ro(x))
        elif func == 'S':
            self.canvas.plot(x, self.solver.s(x))
        elif func == 'z':
            self.canvas.plot(x, self.solver.z(x))

    def scatter(self, x, y):
        self.canvas.scatter(x, y)

