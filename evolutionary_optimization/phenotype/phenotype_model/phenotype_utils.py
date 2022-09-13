from dataclasses import dataclass
from typing import Union, List, Optional

import numpy as np
from numpy import ndarray

from evolutionary_optimization.phenotype import AbstractPhenotype

@dataclass
class PlottingData:
    """Dataclass containing plotting information."""
    x: ndarray
    y: ndarray
    z: Optional[ndarray] = None


def generate_points_for_function(
    phenotype: AbstractPhenotype,
    bottom_plotting_limit: Union[float, int] = -50,
    upper_plotting_limit: Union[float, int] = 50,
    number_of_points: int = 100,
) -> Union[NameError, PlottingData]:
    """Generate datapoints to plot a phenotype function.

    Args:
        phenotype: AbstractPhenotype which we want to plot.
        bottom_plotting_limit: the bottom limit for plotting.
        upper_plotting_limit: the upper limit for plotting.
        number_of_points: number of points to generate within the plotting range.

    Returns:
        Data necessary to generate a plot of the phenotype.

    """
    number_of_dimensions = len(phenotype.genotype.genotype) + 1
    function_data = PlottingData(x=np.empty(0), y=np.empty(0))
    range_of_x = np.linspace(bottom_plotting_limit, upper_plotting_limit, num=number_of_points)

    if number_of_dimensions == 2:
        for x_datapoint in range_of_x:
            function_data.x = np.append(function_data.x, x_datapoint)
            phenotype.genotype.genotype = [x_datapoint]
            phenotype.evaluate_phenotype()
            function_data.y = np.append(function_data.y, phenotype.phenotype_value)

    elif number_of_dimensions == 3:
        function_data.z = np.empty(0)

        x_mesh, y_mesh = np.meshgrid(np.asarray(range_of_x), np.asarray(range_of_x))
        z_mesh = phenotype.evaluate_phenotype_using_arrays(x_mesh, y_mesh)
        function_data.x = x_mesh
        function_data.y = y_mesh
        function_data.z = z_mesh

    else:
        return NameError("You can't plot more than 3 dimensions")

    return function_data
