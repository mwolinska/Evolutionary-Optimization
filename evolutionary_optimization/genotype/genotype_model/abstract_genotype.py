from abc import ABC, abstractmethod
from typing import Tuple, Optional, List, Union


class AbstractGenotype(ABC):
    @abstractmethod
    def __init__(
        self,
        genotype,
        mutation_probability: float,
        ratio_of_population_for_crossover: float,
        number_of_genes: int,
        value_range: Tuple[int, int],
    ):
        """Initialise instance of AbstractGenotype.

        Args:
            genotype: genotype used for mutation, crossover and to calculate phenotype_value.
            mutation_probability: probability of a gene mutating.
            ratio_of_population_for_crossover: ratio of population used for crossover when updating population.
            number_of_genes: number of genes in the genotype.
            value_range: minimum and maximum values of a gene.

        Todo:
            * (Marta): How to deal with genotype typing.
            * (Marta): value range maybe shouldn't be in the constructor
        """
        pass

    @property
    @abstractmethod
    def genotype(self):
        pass

    @genotype.setter
    @abstractmethod
    def genotype(self, value):
        pass

    @classmethod
    @abstractmethod
    def build_random_genotype(
        cls,
        number_of_genes,
        value_range: Tuple[int, int],
        mutation_probability: Optional[float],
        ratio_of_population_for_crossover: Optional[float],
    ) -> "AbstractGenotype":
        """Build random genotype attribute based on class parameters.

        Args:
            number_of_genes: number of genes in the genotype.
            value_range: minimum and maximum values of a gene.
            mutation_probability: probability of a gene mutating.
            ratio_of_population_for_crossover: ratio of population used for crossover when updating population.

        Returns:
            AbstractGenotype object with a randomly generated genotype attribute.
        """
        pass

    @abstractmethod
    def mutate(self):
        """In place modification of the genotype by randomly changing genes based on mutation probability."""
        pass

    @abstractmethod
    def crossover(self, parent_2_genotype: "AbstractGenotype") -> Tuple["AbstractGenotype", "AbstractGenotype"]:
        """Perform crossover between two phenotypes.

        Combines a portion of this object's genotype with that of parent_2 to return 2 new phenotypes
        based on the combined genotypes. The new genotype length is the same as of the parents.

        Args:
            parent_2_genotype: a genotype of the same class whose genotype will be mixed with

        Returns:
            Two new phenotype instances based on the combined genotypes of the two parents.
        """
        pass

    @classmethod
    @abstractmethod
    def from_genotype(
        cls,
        base_genotype: "AbstractGenotype",
        new_genotype: Union[List[int], List[float], List[str]],
    ) -> "AbstractGenotype":
        pass
