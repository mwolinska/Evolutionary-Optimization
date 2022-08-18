import numpy as np
from matplotlib import animation, pyplot as plt, lines


class CreateGif:
    def __init__(self, animation_data_x: np.ndarray, animation_data_y: np.ndarray, static_plot_data: np.ndarray):
        self.fig = plt.figure()
        self.ax = plt.axes(
            xlim=(np.min(static_plot_data[0]), np.max(static_plot_data[0])),
            ylim=(np.min(static_plot_data[1]), np.max(static_plot_data[1])),
        )
        self.time_text = self.ax.text(0.02, 0.95, '', transform=self.ax.transAxes)
        self.best_genotype_text = self.ax.text(0.02, 0.90, '', transform=self.ax.transAxes)
        self.best_phenotype_text = self.ax.text(0.02, 0.85, '', transform=self.ax.transAxes)
        self.line, = self.ax.plot([], [], "ro")
        self.x_data = animation_data_x
        self.y_data = animation_data_y
        self.x = []
        self.y = []
        self.frame_counter = 0
        self.ax.plot(static_plot_data[0], static_plot_data[1])

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
