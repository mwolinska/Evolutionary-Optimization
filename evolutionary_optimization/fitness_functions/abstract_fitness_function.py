from abc import ABC, abstractmethod

from evolutionary_optimization.phenotype.abstract_phenotype import AbstractPhenotype


class AbstractFitnessFunction(ABC):
    @abstractmethod
    def evaluate(self, phenotype: AbstractPhenotype):
        pass
