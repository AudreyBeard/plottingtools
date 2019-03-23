import numpy as np
import plottingtools as pt

data = np.random.randint(1, 10, 6)
labels = ('a', 'b', 'c', 'd', 'e', 'f')

plot = pt.plot.Bars(data=data,
                    labels=labels,
                    title='Simple Example',
                    multicolor=False)
