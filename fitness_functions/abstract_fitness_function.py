from abc import ABC, abstractmethod

from phenotype.abstract_phenotype import AbstractPhenotype


class AbstractFitnessFunction(ABC):
    @abstractmethod
    def evaluate(self, phenotype: AbstractPhenotype):
        pass
