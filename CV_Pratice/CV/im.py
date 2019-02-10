from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

fig = Figure(figsize=(11, 5), dpi=100)


axes = fig.add_subplot(111)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [23, 21, 32, 13, 3, 132, 13, 3, 1]

axes.plot(x, y)
canvas = FigureCanvas(fig)
canvas.draw()
