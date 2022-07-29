from enum import Enum

from evolutionary_optimization.fitness_functions.abstract_fitness_function import AbstractFitnessFunction
from evolutionary_optimization.fitness_functions.implemented_fitness_functions import MaximizeFitnessFunction, MinimizeFitnessFunction, \
    ApproachValueFitnessFunction


class FitnessFunctions(str, Enum):
    """Enum containing implemented fitness functions."""
    MAXIMIZE = "maximize"
    MINIMIZE = "minimize"
    APPROACH_VALUE = "approach_value"

class FitnessFunction:
    """Maps FitnessFunctions to their associated concrete class based on AbstractFitnessFunction."""

    fitness_functions_dictionary = {
            FitnessFunctions.MAXIMIZE: MaximizeFitnessFunction,
            FitnessFunctions.MINIMIZE: MinimizeFitnessFunction,
            FitnessFunctions.APPROACH_VALUE: ApproachValueFitnessFunction,
        }

    @classmethod
    def get_fitness_function(cls, fitness_function: FitnessFunctions) -> type(AbstractFitnessFunction):
        """Return class of desired AbstractFitnessFunction."""
        return cls.fitness_functions_dictionary[fitness_function]
