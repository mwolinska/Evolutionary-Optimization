from abc import ABC, abstractmethod
from typing import Tuple

from evolutionary_optimization.genotype.abstract_genotype import AbstractGenotype

class AbstractPhenotype(ABC):
    @abstractmethod
    def __init__(self, genotype: AbstractGenotype):
        """Initialise AbstractPhenotype object.

        Args
            genotype: an AbstractGenotype that defines the phenotype.
        """
        pass

    @abstractmethod
    def evaluate_phenotype(self):
        """Calculate phenotype value using genotype."""
        pass

    @abstractmethod
    def crossover(self, parent_2: "AbstractPhenotype") -> Tuple["AbstractPhenotype", "AbstractPhenotype"]:
        """Perform crossover between two phenotypes.

        Calls crossover method from the genotype attribute. Combines a portion of this object's genotype
        with that of parent_2 to return 2 new phenotypes based on the combined genotypes.
        The new genotype length is the same as of the parents.

        Args:
            parent_2: a phenotype of the same class whose genotype will be mixed with

        Returns:
            Two new phenotype instances based on the combined genotypes of the two parents.
        """
        pass

    @abstractmethod
    def mutate(self):
        """Randomly change a gene within the genotype based on mutation probability."""
        pass

    @property
    @abstractmethod
    def phenotype_value(self):
        """Stores value of the phenotype based on the genotype - calculated using evaluate_phenotype."""
        pass

    @classmethod
    @abstractmethod
    def from_phenotype(cls, base_phenotype: "AbstractPhenotype"):
        """Create new phenotype with the same attributes as the base phenotype."""
        pass

    # TODO add genotype as a property
