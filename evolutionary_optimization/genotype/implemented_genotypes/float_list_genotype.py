from random import uniform, randint
from typing import Tuple, List, Optional

import numpy as np

from evolutionary_optimization.genotype.genotype_model.genotype_utils import single_point_crossover


class FloatListGenotype:
    def __init__(
            self,
            genotype: Optional[List[float]] = None,
            mutation_probability: float = 0.5,
            ratio_of_population_for_crossover: float = 0,
            number_of_genes: int = 1,
            value_range: Tuple[int, int] = (-10000, 10000),
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
        self._genotype = genotype
        self.mutation_probability = mutation_probability
        self.ratio_of_population_for_crossover = ratio_of_population_for_crossover
        self.number_of_genes = number_of_genes
        self.value_range = value_range

    @property
    def genotype(self):
        """Genotype value used for evaluation of phenotype."""
        return self._genotype

    @genotype.setter
    def genotype(self, value):
        """Genotype attribute setter."""
        self._genotype = value

    @classmethod
    def build_random_genotype(
            cls,
            number_of_genes: int = 1,
            value_range: Tuple[int, int] = (-10000, 10000),
            mutation_probability: float = 0.5,
            ratio_of_population_for_crossover: float = 0,
    ) -> "AbstractGenotype":
        """Build random genotype attribute based on class parameters.

        Args:
            mutation_probability: probability of a gene mutating.
            ratio_of_population_for_crossover: ratio of population used for crossover when updating population.

        Returns:
            AbstractGenotype object with a randomly generated genotype attribute.
        """
        genotype = []

        for i in range(number_of_genes):
            new_gene = uniform(value_range[0], value_range[1])
            genotype.append(new_gene)

        return cls(
            genotype=genotype,
            mutation_probability=mutation_probability,
            ratio_of_population_for_crossover=ratio_of_population_for_crossover,
            number_of_genes=number_of_genes,
            value_range=value_range,
        )

    @classmethod
    def from_genotype(cls, base_genotype: "FloatListGenotype", new_genotype: List[float]) -> "FloatListGenotype":
        """Create a new genotype using the parameters of an existing genotype."""
        return cls(
            genotype=new_genotype,
            value_range=base_genotype.value_range,
            mutation_probability=base_genotype.mutation_probability,
            ratio_of_population_for_crossover=base_genotype.ratio_of_population_for_crossover,
        )

    def mutate(self):
        """In place modification of the genotype by randomly changing genes based on mutation probability."""
        noise = np.random.normal(0, 1, len(self.genotype))
        mutation_mask = np.random.choice([True, False], p=[self.mutation_probability, 1 - self.mutation_probability], size=len(self.genotype)).astype(int)
        mutation_noise = noise * mutation_mask
        self.genotype += mutation_noise

    def crossover(self, parent_2_genotype: "AbstractGenotype") -> Tuple["AbstractGenotype", "AbstractGenotype"]:
        """Perform crossover between two phenotypes.

        Combines a portion of this object's genotype with that of parent_2 to return 2 new phenotypes
        based on the combined genotypes. The new genotype length is the same as of the parents.

        Args:
            parent_2_genotype: a genotype of the same class whose genotype will be mixed with

        Returns:
            Two new phenotype instances based on the combined genotypes of the two parents.
        """
        if len(self.genotype) != len(parent_2_genotype.genotype):
            raise NameError("The Individuals have genotypes of different lengths - crossover is impossible")

        if self.number_of_genes == 1:
            return self, parent_2_genotype
        else:
            last_slice_index = self.number_of_genes - 1
            gene_slice_index = randint(1, last_slice_index)

            child_1_genotype = single_point_crossover(self.genotype, parent_2_genotype.genotype, gene_slice_index)
            child_2_genotype = single_point_crossover(parent_2_genotype.genotype, self.genotype, gene_slice_index)

            child_1 = self.from_genotype(parent_2_genotype, child_1_genotype)
            child_2 = self.from_genotype(parent_2_genotype, child_2_genotype)

            return child_1, child_2
