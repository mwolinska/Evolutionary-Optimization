from dataclasses import dataclass
from typing import Union, List, Optional

import numpy as np
from numpy import ndarray

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
    three_dimensions: bool = False
        # TODO (Marta): remove three_dimensions as a parameter
) -> PlottingData:

    function_data = PlottingData(x=np.empty(0), y=np.empty(0))
    range_of_x = np.linspace(bottom_plotting_limit, upper_plotting_limit, num=number_of_points)

    if not three_dimensions:
        for x_datapoint in range_of_x:
            function_data.x = np.append(function_data.x, x_datapoint)
            phenotype.genotype.genotype = [x_datapoint]
            phenotype.evaluate_phenotype()
            function_data.y = np.append(function_data.x, phenotype.phenotype_value)

    if three_dimensions:
        function_data.z = np.empty(0)

        x_mesh, y_mesh = np.meshgrid(np.asarray(range_of_x), np.asarray(range_of_x))
        z_mesh = phenotype.evaluate_phenotype_using_arrays(x_mesh, y_mesh)
        function_data.x = x_mesh
        function_data.y = y_mesh
        function_data.z = z_mesh

    return function_data
