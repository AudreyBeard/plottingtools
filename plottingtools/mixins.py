import matplotlib.pyplot as plt

# TODO
# [ ] 2020-05-12: support non-perfect subplotting by padding with empty plots

class SubplotMixin(object):
    _initialized = False
    def _init(self, n_plots, max_wh_ratio=2):
        self.n_cols = n_plots
        self.n_rows = n_plots / self.n_cols
        while ((self.n_cols / self.n_rows) > max_wh_ratio) or self.n_rows % 1:
            self.n_cols -= 1
            self.n_rows = n_plots / self.n_cols
            if self.n_cols <= 0:
                raise ValueError("Plots cannot be made into a nice rectangle. There is a solution (pad with empty Axes), but I don't support this yet")
        

    def _subplot(self, y_data, x_data):
        if not self._initialized:
            raise RuntimeError("{} must be initialized before _subplot() is called.".format(self.__class__.__name__))
        
        self.figs, self.axs = plt.subplots(self.n_rows, self.n_cols)
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                axs[i][j].plot()
        
