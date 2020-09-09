# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from numpy import arange, sin, cos, pi
import pyqtgraph as pg
import sys

class Plot2D():
    def __init__(self):
        self.traces = dict()

        #QtGui.QApplication.setGraphicsSystem('raster')
        self.app = QtGui.QApplication([])
        #mw = QtGui.QMainWindow()
        #mw.resize(800,800)

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.win.resize(1000,600)
        self.win.setWindowTitle('pyqtgraph example: Plotting')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        self.canvas = self.win.addPlot(title="Pytelemetry")

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def trace(self,name,dataset_x,dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x,dataset_y)
        else:
            self.traces[name] = self.canvas.plot(pen='y')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    p = Plot2D()
    i = 0
    a = 1     #振幅
    fs = 96 * (10**3) #サンプリング周波数
    f0 =  20 #周波数
    sec = 0.005  #秒
    tpi = 2 * np.pi
    la = 10 #波長
    T = 2 #周期
    time = 1 #時刻

    def update():
        global
        t = np.arange(0,3.0,0.01)
        s = sin(2 * pi * t + i)
        c = cos(2 * pi * t + i)
        sc = s + c
        xandy = a * np.sin( 2 * np.pi * (time / T - t / la ))
        # p.trace("sin",t,s)
        # p.trace("cos",t,c)
        # p.trace("sin+cos",t,sc)
        p.trace("xy",t,sc)

        i += 0.1

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)

    p.start()