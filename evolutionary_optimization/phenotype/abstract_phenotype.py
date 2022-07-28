from abc import ABC, abstractmethod
from typing import Tuple

from evolutionary_optimization.genotype.abstract_genotype import AbstractGenotype

class AbstractPhenotype(ABC):
    @abstractmethod
    def __init__(self, genotype: AbstractGenotype):
        pass

    @abstractmethod
    def evaluate_phenotype(self):
        pass

    @abstractmethod
    def crossover(self, parent_2: "AbstractPhenotype") -> Tuple["AbstractPhenotype", "AbstractPhenotype"]:
        pass

    @abstractmethod
    def mutate(self):
        pass

    @property
    @abstractmethod
    def phenotype_value(self):
        pass

    @classmethod
    @abstractmethod
    def from_phenotype(cls, base_phenotype: "AbstractPhenotype"):
        pass

    # TODO add genotype as a property
