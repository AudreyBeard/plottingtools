import plottingtools as pt
import numpy as np


length = 25
n_lines = 4
y = [np.arange(length) - np.random.randint(length, size=length) for i in range(n_lines)]
x = np.arange(length, length + length)
labels = ['Line {}'.format(i) for i in range(n_lines)]
line_formats = ['--', 'b.-', 'rd', 'k:']

kwargs = dict(plot_type='lines',
              y=y,
              x=x,
              title='Advanced example',
              labels=labels,
              xlabel='x-axis',
              ylabel='y-axis',
              line_formats=line_formats,
              )

if __name__ == "__main__":
    plot = pt.plot.Lines(**kwargs)
