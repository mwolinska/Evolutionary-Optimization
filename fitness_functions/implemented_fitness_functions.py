from fitness_functions.abstract_fitness_function import AbstractFitnessFunction
from phenotype.abstract_phenotype import AbstractPhenotype


class MaximizeFitnessFunction(AbstractFitnessFunction):
    def evaluate(self, phenotype: AbstractPhenotype):
        return phenotype.phenotype_value


class MinimizeFitnessFunction(AbstractFitnessFunction):
    def evaluate(self, phenotype: AbstractPhenotype):
        return phenotype.phenotype_value * -1


class ApproachValueFitnessFunction(AbstractFitnessFunction):
    def evaluate(self, phenotype: AbstractPhenotype):
        return 1 / (phenotype.expected_value - phenotype.phenotype_value)
