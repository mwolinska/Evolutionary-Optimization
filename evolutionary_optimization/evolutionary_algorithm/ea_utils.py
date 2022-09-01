import numpy as np
from matplotlib import animation, pyplot as plt, lines, cm

from evolutionary_optimization.phenotype.phenotype_model.phenotype_utils import PlottingData


class CreateGif2D:
    def __init__(self, animation_data_x: np.ndarray, animation_data_y: np.ndarray, static_plot_data: PlottingData):
        self.fig, self.ax = plt.subplots()

        self.ax.set_xlim((np.min(static_plot_data.x), np.max(static_plot_data.x)))
        self.ax.set_ylim((np.min(static_plot_data.y), np.max(static_plot_data.y)))

        self.time_text = self.ax.text(0.02, 0.95, '', transform=self.ax.transAxes)
        self.best_genotype_text = self.ax.text(0.02, 0.90, '', transform=self.ax.transAxes)
        self.best_phenotype_text = self.ax.text(0.02, 0.85, '', transform=self.ax.transAxes)
        self.line, = self.ax.plot([], [], "ro")

        self.x_data = animation_data_x
        self.y_data = animation_data_y
        self.x = []
        self.y = []

        self.ax.plot(static_plot_data.x, static_plot_data.y)

    def plot_background_for_frame(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self, i):
        self.x = self.x_data[i]
        self.y = self.y_data[i]
        self.line.set_data(self.x, self.y)
        self.time_text.set_text("epoch = " + str(i))
        self.best_genotype_text.set_text("best genotype = %f" % self.x)
        self.best_phenotype_text.set_text("best phenotype = %f" % self.y)
        return self.line, self.time_text, self.best_genotype_text, self.best_phenotype_text

    def generate_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.plot_background_for_frame,
                                       frames=len(self.x_data), interval=200, blit=True)
        # anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
        plt.show()

class CreateGif3D:
    def __init__(
            self,
            animation_data_x: np.ndarray,
            animation_data_y: np.ndarray,
            animation_data_z: np.ndarray,
            static_plot_data: PlottingData
        self.fig, self.ax = plt.subplots(constrained_layout=True)
        self.ax = plt.axes(projection="3d")
        self.x_data = animation_data_x
        self.y_data = animation_data_y
        self.z_data = animation_data_z
        self.static_data = static_plot_data
    def generate_animation(self):
        raise NotImplementedError