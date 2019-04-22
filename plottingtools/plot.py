# plotting.py
# Author: Joshua Beard
# Created: 2019-01-08

# TODO:
# [ ] Support multiple x arrays
# [ ] ylim for Lines
# [ ] max_val_pad for Lines
# [x] Match API for Bars with Lines
# [ ] Offload common methods to Plot2D superclass
# [ ] Better placement of on-chart text relative to bar height
# [ ] Support for "below"-bar on-chart text
# [x] Test non-scaled bars
# [ ] different logic if labels are numbers as opposed to strings?
# [x] support show=False
# [x] init of Plot2D should use a kwarg

from matplotlib import pyplot as plt
from . import util
from collections import Iterable
import numpy as np
import warnings
from os.path import join as pathjoin

DEBUG = False
if DEBUG:
    import ipdb


def close_all():
    plt.close('all')


class Plot2D(object):
    def __init__(self, **kwargs):
        # TODO do as much of the init stuff here as possible - reduce the size
        # of the codebase and make it easier to read

        try:
            constraints = {'x': Iterable,
                           'y': Iterable,
                           'labels': Iterable,
                           'figsize': Iterable,
                           'title': str,
                           'ylim': Iterable,
                           'max_val_pad': (int, float, '>=0'),
                           'show_bottom_labels': bool,
                           'show_legend': bool,
                           'show': bool,
                           'save': bool,
                           'save_name': str,
                           'xlabel': str,
                           'ylabel': str,
                           'save_path': str,
                           }
            constraints.update(self.constraints)
        except AttributeError:
            pass
        finally:
            self.constraints = constraints

        try:
            defaults = {'x': None,
                        'y': None,
                        'labels': None,
                        'figsize': (12, 8),
                        'title': '',
                        'ylim': None,
                        'max_val_pad': 0,
                        'show_bottom_labels': False,
                        'show_legend': True,
                        'show': True,
                        'save': False,
                        'save_name': None,
                        'xlabel': None,
                        'ylabel': None,
                        'save_path': '.',
                        }
            defaults.update(self.defaults)
        except AttributeError:
            pass
        finally:
            self.defaults = defaults

        self.params = util.ParameterRegister(self.constraints,
                                             self.defaults,
                                             accept_none=True,
                                             match_all_constraints=False)
        self.params.set(**kwargs)
        self.params.set_uninitialized_params()

        #self._fig = plt.figure(figsize=self.params['figsize'])
        #self._ax = self._fig.add_subplot(111)
        self._fig, self._ax = plt.subplots(figsize=self.params['figsize'])
        self._data = []

        if self.params['save_name'] is None:
            self._savename = pathjoin(self.params['save_path'],
                                      'graph_' + '_'.join(self.params['title'].split(' ')))
        else:
            self._savename = pathjoin(self.params['save_path'], self.params['save_name'])

    def set_fig_props(self):
        self.set_labels()
        self.set_title()
        self.set_ticks()

    def show(self):
        plt.show()

    def save(self, savename=None):
        if savename is not None:
            self._savename = savename

        plt.savefig(self._savename)

    def set_title(self):
        self._fig.suptitle(self.params['title'], fontsize=max(self.params['figsize']))

    def close(self):
        plt.close(self._fig)

    def clear(self):
        self._fig.clf()

    def set_legend(self, labels=None):
        labels = self.params['labels'] if labels is None else labels
        if labels is not None:
            self._ax.legend(self._data, labels,
                            prop={'size': max(self.params['figsize'])})

    def set_labels(self, xlabels=None, ylabels=None):
        # x- and y-axis labels
        xl = None
        yl = None
        if xlabels is None and self.params['xlabel'] is not None:
            xl = self._ax.set_xlabel(self.params['xlabel'])
        elif xlabels:
            xl = self._ax.set_xlabel(xlabels)
        if ylabels is None and self.params['ylabel'] is not None:
            yl = self._ax.set_ylabel(self.params['ylabel'])
        elif ylabels:
            yl = self._ax.set_ylabel(ylabels)
        return xl, yl

    def set_ticks(self, xticks=None, yticks=None):
        sane_ticks = self._get_ticks_sane()
        if xticks is None:
            xticks = sane_ticks[0]
        if yticks is None:
            yticks = sane_ticks[1]
        self._ax.set_xticks(xticks)
        self._ax.set_yticks(yticks)
        self._ax.tick_params(labelsize=max(self.params['figsize']))

    def _get_ticks_sane(self):
        n_xticks = self.params['figsize'][0] + 1
        n_yticks = self.params['figsize'][1] + 1
        min_x = np.array(self.params['x']).min()
        max_x = np.array(self.params['x']).max()
        min_y = np.array(self.params['y']).min()
        max_y = np.array(self.params['y']).max()
        if max_x >= n_xticks:
            stride = (max_x - min_x) // n_xticks
            xticks = np.arange(min_x, max_x + 1, stride)
        else:
            xticks = np.linspace(min_x, max_x, self.params['figsize'][0] + 1)
        if max_y >= n_yticks:
            stride = (max_y - min_y) // n_yticks
            yticks = np.arange(min_y, max_y + 1, stride)
        else:
            yticks = np.linspace(min_y, max_y, self.params['figsize'][1] + 1)
        return (xticks, yticks)


class Bars(Plot2D):
    """
        Plots separate bars as independent categories, coloring them differently
        Parameters:
            data: <list>, <tuple>, or <np.ndarray> of the bar heights
            labels: <list>, <tuple>, or <np.ndarray> of labels for the different bars (optionally displayed)
            bar_width: <int> or <float> defining bar width
            figsize: <list>, <tuple>, or <np.ndarray> of figure size
            title: <str> defining the graph title, which is scaled based on figure size. If save_name is not defined, but save==True, this is also the save name
            ylim: <list>, <tuple>, or <np.ndarray> of y limits, None does autoscaling
            max_val_pad: <int> or <float> defining the proportional padding above the max value. Autoscaling uses 0.1
            sort_by: <str>, <tuple>, <list>, <np.ndarray> defining order of data displayed ('ascending' or 'descending', or some canonical ordering). None does no sorting
            show_bottom_labels: <bool> switch for displaying labels at the bottom
            show_legend: <bool> switch for displaying legend
            show_max_val: <bool> switch for displaying dashed line at maximum value
            show: <bool> whether to show the plot NOTE: as of version 0.1.2, setting this to False does nothing
            save: <bool> whether to save the plot
            scale_by: <int>, <float>, <tuple>, <list>, <np.ndarray> the factor by which to scale the data. Note this must be broadcastable to the data
            show_bar_labels: <bool> switch for displaying labels at top of each bar
            bar_label_format: function format for bars label. If None, displays raw data
            show_as_percent: <bool> scales everything as percentages
        Returns: Nothing
    """

    # Bars-specific constraints and defaults - some of these are duplicated,
    # but kept because I may phase them out in the superclass
    constraints = {'bar_width': util.isnumeric,
                   'max_val_pad': util.isnumeric,
                   'sort_by': ('ascending', 'descending', Iterable),
                   'show_bottom_labels': bool,
                   'show_legend': bool,
                   'show_max_val': bool,
                   'scale_by': (util.isnumeric, Iterable),
                   'show_bar_labels': bool,
                   'bar_label_format': (lambda x: x),
                   'multicolor': bool,
                   'show_as_percent': bool,
                   }
    defaults = {'bar_width': 0.75,
                'max_val_pad': 0.1,
                'sort_by': None,
                'show_bottom_labels': True,
                'show_legend': False,
                'show_max_val': False,
                'scale_by': None,
                'show_bar_labels': False,
                'bar_label_format': None,
                'multicolor': True,
                'show_as_percent': False,
                }

    def __init__(self, **kwargs):
        # Super has a number of kwarg constraints and defaults
        super().__init__(**kwargs)

        try:
            # TODO this is deprecated
            self.params['y'] = np.array(self.params['data'])
            warnings.warn("using 'data' to pass bar height to plotting object is deprecated. Use 'y' instead - overriding 'y'")

        except KeyError:
            # NOTE this is the preferred keyword argument, as it more closely follows the API for Lines
            self.params['y'] = np.array(self.params['y'])
        finally:
            y_vals = self.params['y']

        labels = np.array(self.params['labels']) if self.params['labels'] is not None else None

        # Sort the data and labels by ascending, descending, or the user-defined order
        if self.params['sort_by'] is not None:
            if isinstance(self.params['sort_by'], str):
                order = np.argsort(y_vals)
                if self.params['sort_by'].lower() == 'descending':
                    order = order[::-1]
            else:
                order = np.array(self.params['sort_by'])
            y_vals = y_vals[order]
            labels = labels[order] if labels is not None else None

        # If user wants labels shown at the bottom of the plot
        if self.params['show_bottom_labels'] and labels is not None:
            if len(labels) != len(y_vals):
                raise ValueError('len(labels) = {} but len(y_vals) = {}'.format(len(labels), len(y_vals)))

            bottom_labels = [labels[i] + '\nN = {}'.format(y_vals[i])
                             for i in range(len(labels))]

        else:
            bottom_labels = None  # NOQA

        scale_factor = np.array(self.params['scale_by']) if self.params['scale_by'] is not None else None
        if scale_factor is not None:
            if scale_factor.size != len(labels) and scale_factor.size > 1:
                raise ValueError('scale_by (shape {}) must be broadcastable to y_vals (shape {})'.format(scale_factor.shape, y_vals.shape))

            y_vals = y_vals / scale_factor
            max_val = 1
        else:
            max_val = y_vals.max()

        # If we're displaying percentages, scale the y-axis accordingly
        ylim = self.params['ylim']
        if self.params['show_as_percent']:
            y_vals *= 100
            if ylim is not None:
                ylim = (ylim[0] * 100, ylim[1] * 100)

        # If ylim is not specified, autoscale
        if DEBUG:
            ipdb.set_trace()

        if ylim is None:
            ylim = (0, max(y_vals) + max(y_vals) * self.params['max_val_pad'])

        # Now let's plot the damn thing
        if self.params['x'] is None:
            offsets = list(range(y_vals.size))
            self.params['x'] = np.array(offsets)
        else:
            offsets = self.params['x']

        if self.params['multicolor']:
            for i in range(len(labels)):
                self._data.append(self._ax.bar(offsets[i],
                                               y_vals[i],
                                               self.params['bar_width']))
        else:
            self._data = self._ax.bar(offsets, y_vals,
                                      self.params['bar_width'])

        # Show a line at the maximum value
        if self.params['show_max_val']:
            max_val = 100 if self.params['show_as_percent'] else max_val
            self._ax.plot([min(offsets) - 1, max(offsets) + 1],
                          [max_val, max_val],
                          '--',
                          color=[0.75, 0.75, 0.75])

        # Text drawn on the graph labeling the bars with their y_vals
        if self.params['show_bar_labels']:

            # bar_label_format should either be None or some function
            if self.params['bar_label_format'] is not None:
                fmt = self.params['bar_label_format']
            else:
                def fmt(x):
                    return '{}'.format(x)

            if scale_factor != np.array(None):
                y_offset = 0.05

            for i in range(y_vals.size):
                self._ax.text(x=offsets[i], y=y_vals[i] + y_offset, s=fmt(y_vals[i]))

        # Limits and tick spacing
        self._ax.set_ylim(ylim)
        self._ax.set_xlim(offsets[0] - self.params['bar_width'],
                          offsets[-1] + self.params['bar_width'])
        self.set_ticks(xticks=offsets)

        # Using a legend
        if self.params['show_legend']:
            self.set_legend(labels)

        self.set_labels()
        self.set_title()

        # Saving uses title if save_name is not defined
        if self.params['save']:
            self.save()

        if self.params['show']:
            self.show()


class Lines(Plot2D):
    # No Lines-specific constraints or defaults since there's not a lot of
    # customization that I offer yet.

    constraints = {'line_formats': Iterable,
                   }
    defaults = {'line_formats': '-',
                }

    def __init__(self, **kwargs):
        # Super has a number of kwarg constraints and defaults
        super().__init__(**kwargs)

        # Grab all lines given as a list for easier logic later
        try:
            y_vals = [vec for vec in self.params['y']]
        except TypeError:
            y_vals = [self.params['y']]

        # If x is not given, default to nonnegative integers
        if self.params['x'] is None:
            x_vals = np.arange(len(y_vals[0]))
        else:
            x_vals = self.params['x']

        # If labels are not given, set to blank for simpler plotting
        if self.params['labels'] is None:
            labels = ['' for i in range(len(y_vals))]
        else:
            labels = self.params['labels']

        # If only a single label is given, turn it into a list for easier logic
        labels = [labels] if isinstance(labels, str) else labels

        # Get line formats as list
        line_formats = self.params['line_formats']
        if isinstance(line_formats, str):
            line_formats = [line_formats for i in range(len(y_vals))]

        # Do the plotting
        # This allows users to specify specific x-values for each curve -
        # x_vals must be same length as y_vals
        if util.isiterable(x_vals[0]):
            for (x, y, label, fmt) in zip(x_vals, y_vals, labels, line_formats):
                self._data.append(self._ax.plot(x, y, fmt, label=label))
        else:
            if util.isiterable(y_vals[0]):
                for (y, label, fmt) in zip(y_vals, labels, line_formats):
                    self._data.append(self._ax.plot(x_vals, y, fmt, label=label))
            else:
                self._data.append(self._ax.plot(x_vals, y_vals, line_formats[0], label=labels))

        self.set_legend()
        self.set_labels()
        self.set_title()
        self.set_ticks()

        # Save and show now if needed
        if self.params['save']:
            self.save()

        if self.params['show']:
            self.show()


class Scatter(Plot2D):
    constraints = {'marker_formats': Iterable,
                   }
    defaults = {'marker_formats': None,
                }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title()

    def plot(self, x=None, y=None, color=None, labels=None, marker_formats=None):
        assert x is not None and y is not None
        self._data.append(self._ax.scatter(x=x,
                                           y=y,
                                           c=color,
                                           marker=marker_formats,
                                           label=labels))

    def _get_x(self, y, low=0):
        x = np.arange(low, len(y) + low)
        return x
