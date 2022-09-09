import numpy as np
from matplotlib import animation, pyplot as plt, lines, cm

from evolutionary_optimization.phenotype.phenotype_model.phenotype_utils import PlottingData


class CreateGif2D:
    def __init__(self, animation_data_x: np.ndarray, animation_data_y: np.ndarray, static_plot_data: PlottingData):
        """Initialises CreateGif2D class.

        This class creates a gif of a two-dimensional phenotype.

        Args:
            animation_data_x: genotype value to be lapsed in the gif.
            animation_data_y: phenotype value to be lapsed in the gif.
            static_plot_data: data to be used in the background of the gif e.g. the phenotype function.
        """

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
        """Initialises the background for the gif."""
        self.line.set_data([], [])
        return self.line,

    def animate(self, i):
        """Function called at each frame, plots the best phenotype / genotype pair."""
        self.x = self.x_data[i]
        self.y = self.y_data[i]
        self.line.set_data(self.x, self.y)
        self.time_text.set_text("epoch = " + str(i))
        self.best_genotype_text.set_text("best genotype = %f" % self.x)
        self.best_phenotype_text.set_text("best phenotype = %f" % self.y)
        return self.line, self.time_text, self.best_genotype_text, self.best_phenotype_text

    def generate_animation(self):
        """Generates gif animation."""
        anim = animation.FuncAnimation(
            self.fig,
            self.animate,
            init_func=self.plot_background_for_frame,
            frames=len(self.x_data),
            interval=200,
            blit=True,
        )

        plt.show()


class CreateGif3D:
    def __init__(
            self,
            animation_data_x: np.ndarray,
            animation_data_y: np.ndarray,
            animation_data_z: np.ndarray,
            static_plot_data: PlottingData
    ):
        # self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
        self.fig, self.ax = plt.subplots(constrained_layout=True)
        self.ax = plt.axes(projection="3d")
        self.ax = plt.axes(
            xlim=(np.min(static_plot_data.x), np.max(static_plot_data.x)),
            ylim=(np.min(static_plot_data.y), np.max(static_plot_data.y)),
            zlim=(np.min(static_plot_data.z), np.max(static_plot_data.z))
        )
        self.time_text = self.ax.text(0.02, 0.95, '', transform=self.ax.transAxes)
        self.best_genotype_text = self.ax.text(0.02, 0.90, '', transform=self.ax.transAxes)
        self.best_phenotype_text = self.ax.text(0.02, 0.85, '', transform=self.ax.transAxes)
        self.line = self.ax.plot([], [], [])
        self.x_data = animation_data_x
        self.y_data = animation_data_y
        self.z_data = animation_data_z
        self.x = []
        self.y = []
        self.z = []
        self.static_data = static_plot_data
        self.ax.plot_surface(self.static_data.x, self.static_data.y, self.static_data.z, cmap=cm.coolwarm, rstride=1,
                             cstride=1, edgecolor="none", alpha=0.7)

    # def plot_background_for_frame(self):
    #     self.line._offsets3d = ([], [], [])
    #     return self.line,

    def animate(self, i):
        self.ax.clear()
        self.x = self.x_data[i]
        self.y = self.y_data[i]
        self.z = self.z_data[i]

        self.ax.text(0.89, 0.84, f"epoch = {i}")

        # self.line, = self.ax.plot3D(self.x, self.y, self.z, "ro")
        # self.line.set_data(self.x, self.y, self.z)
        # self.line._offsets3d = (self.x, self.y, self.z)
        self.ax.plot3D(self.x, self.y, self.z, marker="+", color="black")
        # self.line.set_data([self.x, self.y, self.z])
        # self.line.set_3d_properties([self.x, self.y, self.z])
        # self.time_text.set_text("epoch = " + str(i))
        # self.best_genotype_text.set_text("best genotype = %f" % self.x)
        # self.best_phenotype_text.set_text("best phenotype = %f" % self.y)
        # return self.line
        self.ax.plot_surface(self.static_data.x, self.static_data.y, self.static_data.z, cmap=cm.coolwarm, rstride=1, cstride=1, edgecolor="none", alpha=0.7)

    def generate_animation(self):
        raise NotImplementedError

        # anim = animation.FuncAnimation(self.fig, self.animate,
        #                                frames=len(self.x_data), interval=200)
        # # anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
        # plt.show()
