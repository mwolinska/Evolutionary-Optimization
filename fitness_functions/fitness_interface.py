from enum import Enum

from fitness_functions.abstract_fitness_function import AbstractFitnessFunction
from fitness_functions.implemented_fitness_functions import MaximizeFitnessFunction, MinimizeFitnessFunction, \
    ApproachValueFitnessFunction


class FitnessFunctions(str, Enum):
    MAXIMIZE = "maximize"
    MINIMIZE = "minimize"
    APPROACH_VALUE = "approach_value"

class FitnessFunction:

    fitness_functions_dictionary = {
            FitnessFunctions.MAXIMIZE: MaximizeFitnessFunction,
            FitnessFunctions.MINIMIZE: MinimizeFitnessFunction,
            FitnessFunctions.APPROACH_VALUE: ApproachValueFitnessFunction,
        }

    @classmethod
    def get_fitness_function(cls, fitness_function: FitnessFunctions) -> type(AbstractFitnessFunction):
        return cls.fitness_functions_dictionary[fitness_function]
