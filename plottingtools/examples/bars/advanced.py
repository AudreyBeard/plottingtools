import numpy as np
import plottingtools as pt

data = np.random.randint(1, 10, 6)
labels = ('a', 'b', 'c', 'd', 'e', 'f')

pt.plot.bars(data,
             labels,
             title='Intermediate Example',
             show_bottom_labels=True,
             show_max_val=True,
             show_as_percent=True,
             scale_by=max(data),
             ylim=[0, 1.1],
             show_bar_labels=True,
             bar_label_format=lambda x: '{:.2f} Percent'.format(x),
             sort_by=[3, 2, 5, 4, 0, 1],)
