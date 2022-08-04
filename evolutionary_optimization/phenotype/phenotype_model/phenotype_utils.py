from typing import Union

import numpy as np

from evolutionary_optimization.phenotype import AbstractPhenotype

@dataclass
class PlottingData:
    x: ndarray
    y: ndarray
    z: Optional[ndarray] = None

def generate_points_for_function(
        phenotype: AbstractPhenotype,
        bottom_plotting_limit: Union[float, int] = -50,
        upper_plotting_limit: Union[float, int] = 50,
        number_of_points: int = 100,
    ):
    x_values_for_plot = []
    y_values_for_plot = []

    range_of_x = np.linspace(bottom_plotting_limit, upper_plotting_limit, num=number_of_points)

    for x in range_of_x:
        x_values_for_plot.append(x)
        phenotype.genotype.genotype = [x]
        phenotype.evaluate_phenotype()
        y_value = phenotype.phenotype_value
        y_values_for_plot.append(y_value)

    return x_values_for_plot, y_values_for_plot
