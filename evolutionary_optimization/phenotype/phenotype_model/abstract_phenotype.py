from abc import ABC, abstractmethod
from typing import Tuple

from numpy import ndarray

from evolutionary_optimization.genotype.genotype_model.abstract_genotype import AbstractGenotype

class AbstractPhenotype(ABC):
    @abstractmethod
    def __init__(self, genotype: AbstractGenotype):
        """Initialise AbstractPhenotype object.

        Args
            genotype: an AbstractGenotype that defines the phenotype.
        """
        pass

    @property
    @abstractmethod
    def genotype(self):
        """Abstract genotype that defines the phenotype."""
        pass

    @genotype.setter
    @abstractmethod
    def genotype(self, value):
        """Genotype property setter."""
        pass

    @property
    @abstractmethod
    def phenotype_value(self):
        """Stores value of the phenotype based on the genotype - calculated using evaluate_phenotype."""
        pass

    @phenotype_value.setter
    @abstractmethod
    def phenotype_value(self, value):
        """Phenotype_value setter."""
        pass

    @abstractmethod
    def evaluate_phenotype(self):
        """Calculate phenotype value using genotype."""
        pass

    @abstractmethod
    def crossover(self, parent_2: "AbstractPhenotype") -> Tuple["AbstractPhenotype", "AbstractPhenotype"]:
        """Perform crossover between two phenotypes.

        Calls crossover method from the genotype attribute.

        Args:
            parent_2: a phenotype of the same class whose genotype will be mixed with

        Returns:
            Two new phenotype instances based on the combined genotypes of the two parents.
        """
        pass

    @abstractmethod
    def mutate(self):
        """In place modification of the genotype by randomly changing genes based on mutation probability."""
        pass

    @classmethod
    @abstractmethod
    def from_phenotype(cls, base_phenotype: "AbstractPhenotype"):
        """Create new phenotype with the same attributes as the base phenotype."""
        pass

    @staticmethod
    @abstractmethod
    def evaluate_phenotype_using_arrays(x_values: ndarray, y_values: ndarray) -> ndarray:
        """Calculate multiple phenotype values from numpy arrays."""
        pass
