import plottingtools as pt
import numpy as np


length = 25
y = np.arange(length) - np.random.randint(length, size=length)
x = np.arange(length, length + length)

kwargs = dict(plot_type='lines',
              y=y,
              x=x,
              title='Intermediate example',
              labels='Single line',
              xlabel='x-axis',
              ylabel='y-axis',
              )

if __name__ == "__main__":
    plot = pt.plot.Lines(**kwargs)
