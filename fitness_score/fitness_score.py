from enum import Enum

from individual import Individual
from phenotype.phenotypes_interface import Phenotypes


class FitnessFunction(Enum):
    MAXIMIZE = "maximize"
    MINIMIZE = "minimize"
    APPROACH_VALUE = "approach_value"

class FitnessScore:
    def __init__(self, individual: Individual, fitness_function: FitnessFunction = None):

        self.phenotype = individual.phenotype
        self.phenotype_value = individual.phenotype_value
        self.fitness_function = fitness_function if fitness_function is not None else self.get_fitness_function()

    def calculate_score(self):
        if self.fitness_function == FitnessFunction.MAXIMIZE:
            fitness_score = self.phenotype_value
        elif self.fitness_function == FitnessFunction.MINIMIZE:
            fitness_score = abs(self.phenotype_value)
        else:
            raise NotImplementedError
        return fitness_score

    def get_fitness_function(self):
        if self.phenotype == Phenotypes.MSE:
            return FitnessFunction.MINIMIZE
        elif self.phenotype == Phenotypes.TEST:
            return FitnessFunction.MAXIMIZE
        else:
            return FitnessFunction.MAXIMIZE
