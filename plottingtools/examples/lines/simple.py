import plottingtools as pt
import numpy as np


length = 25
x = np.arange(length)
y = np.arange(length) - np.random.randint(length, size=length)

kwargs = dict(plot_type='lines',
              x=x,
              y=y,
              title='Witty Title',
              )

if __name__ == "__main__":
    plot = pt.plot.Plot2D(**kwargs)
