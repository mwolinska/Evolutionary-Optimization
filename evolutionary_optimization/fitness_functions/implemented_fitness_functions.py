from typing import Union

from evolutionary_optimization.fitness_functions.abstract_fitness_function import AbstractFitnessFunction
from evolutionary_optimization.phenotype.phenotype_model.abstract_phenotype import AbstractPhenotype


class MaximizeFitnessFunction(AbstractFitnessFunction):
    def evaluate(self, phenotype: AbstractPhenotype) -> Union[float, int]:
        """Looking for maximum phenotype value.

        Args:
            phenotype: instance of Abstract phenotype being evaluated).

        Returns:
            The phenotype_value directly as we are looking for the greatest value.
        """
        return phenotype.phenotype_value


class MinimizeFitnessFunction(AbstractFitnessFunction):
    def evaluate(self, phenotype: AbstractPhenotype) -> Union[float, int]:
        """Looking for minimum phenotype value.

        Args:
            phenotype: instance of Abstract phenotype being evaluated).

        Returns:
            The negative version of phenotype_value as we are looking for the lowest value i.e.
                the most negative phenotype will become the greatest fitness score.
        """
        return phenotype.phenotype_value * -1


class ApproachValueFitnessFunction(AbstractFitnessFunction):
    def __init__(self, expected_value: Union[float, int]):
        self.expected_value = expected_value

    def evaluate(self, phenotype: AbstractPhenotype) -> float:
        return 1 / abs(self.expected_value - phenotype.phenotype_value)
