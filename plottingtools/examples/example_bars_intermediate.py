import numpy as np
import plottingtools as pt

data = np.random.randint(1, 10, 6)
labels = ('a', 'b', 'c', 'd', 'e', 'f')

pt.plot.bars(data,
             labels,
             title='Intermediate Example',
             show_legend=True,
             sort_by='descending',
             max_val_pad=1,
             show_bottom_labels=False,
             show_max_val=True)
