from random import randint
from typing import Tuple, Optional, List

import numpy as np

from evolutionary_optimization.genotype.abstract_genotype import AbstractGenotype


class IntegerListGenotype(AbstractGenotype):

    def __init__(
        self,
        genotype: Optional[List[int]] = None,
        mutation_probability: float = 0.1,
        ratio_of_population_for_crossover: float = 0.5,
        number_of_genes: int = 1,
        value_range: Tuple[int, int] = (0, 9),
    ):

        self.genotype = genotype
        self.mutation_probability = mutation_probability
        self.ratio_of_population_for_crossover = ratio_of_population_for_crossover
        self.number_of_genes = number_of_genes
        self.value_range = value_range

    # TODO do I indent functions like the init? What about within code
    @classmethod
    def build_random_genotype(cls,# TODO set infinity
                              number_of_genes: int = 1,
                              value_range: Tuple[int, int] = (-100, 100),
                              mutation_probability: Optional[float] = 0.5,
                              ratio_of_population_for_crossover: Optional[float] = 0.5
                              ) -> "IntegerListGenotype":
        """Builds genotype based on requirements defined by genotype_properties."""
        genotype = []

        for i in range(number_of_genes):
            new_gene = randint(value_range[0], value_range[1])
            genotype.append(new_gene)

        return cls(genotype=genotype,
                   mutation_probability=mutation_probability,
                   ratio_of_population_for_crossover=ratio_of_population_for_crossover,
                   number_of_genes=number_of_genes,
                   value_range=value_range)

    def mutate(self):
        new_genotype = []

        for gene in self.genotype:
            mutation = np.random.choice([True, False], p=[self.mutation_probability, 1 - self.mutation_probability])

            if mutation:
                new_gene = randint(self.value_range[0], self.value_range[1])
            else:
                new_gene = gene

            new_genotype.append(new_gene)
        self.genotype = new_genotype

    def crossover(self,
                  parent_2: "IntegerListGenotype",
                  ) -> Tuple["IntegerListGenotype", "IntegerListGenotype"]:
        """Performs single point crossover operation for 1 set of parents.

        A random integer is generated to split the genotype of the two individuals -
        this is the gene slice index. Then two child Individuals are generated with the complementary parts
        of the parent individuals. If the parent's genotype length is 1, cross over is impossible so the parent
        instances are returned.

        Example:
            parent_1.genotype = [1, 2, 3, 4]
            parent_2.genotype = [A, B, C, D]
            gene_slice_index = 1

            child_1.genotype = [1, B, C, D]
            child_2.genotype = [A, 2, 3, 4]

        Args:
            parent_1: Individual which will be used to create an offspring.
            parent_2: Individual which will be used to create an offspring.

        Returns:
            Tuple of AbstractGenotype.
        """
        if len(self.genotype) != len(parent_2.genotype):
            raise NameError("The Individuals have genotypes of different lengths - crossover is impossible")

        if self.number_of_genes == 1:
            return self, parent_2
        else:
            last_slice_index = self.number_of_genes - 1
            gene_slice_index = randint(1, last_slice_index)

            child_1_genotype = self.single_point_crossover(self.genotype, parent_2.genotype, gene_slice_index)
            child_2_genotype = self.single_point_crossover(parent_2.genotype, self.genotype, gene_slice_index)

            child_1 = IntegerListGenotype(genotype=child_1_genotype,
                                          mutation_probability=self.mutation_probability,
                                          ratio_of_population_for_crossover=self.ratio_of_population_for_crossover,
                                          number_of_genes=self.number_of_genes,
                                          value_range=self.value_range)

            child_2 = IntegerListGenotype(genotype=child_2_genotype,
                                          mutation_probability=self.mutation_probability,
                                          ratio_of_population_for_crossover=self.ratio_of_population_for_crossover,
                                          number_of_genes=self.number_of_genes,
                                          value_range=self.value_range)
            # TODO implement method to return Genotype copy with updated genotype attribuet

            return child_1, child_2

    @staticmethod
    def single_point_crossover(parent_1_genotype: List[int], parent_2_genotype: List[int], gene_slice_index: int) -> List[int]:
        """A single point crossover for genotype of type list.

        This is a single point crossover. Using the gene_slice_index, for both parents the genotype.all genes are sliced.
        The slice [:gene_slice_index[ is taken from parent_1 and the slice [gene_slice_index:] is taken from parent_2.
        The two complementary slices are then joined to create a new individual (a child) from the new genotype.

        Args:
            parent_1_genotype: Individual which will be used to create an offspring.
            parent_2_genotype: Individual which will be used to create an offspring.
            gene_slice_index: random integer at which the parent genotypes will be sliced.

        Returns:
            An Individual instance.
        """
        child_genotype_part_1 = parent_1_genotype[:gene_slice_index]
        child_genotype_part_2 = parent_2_genotype[gene_slice_index:]
        child_genotype = child_genotype_part_1 + child_genotype_part_2
        return child_genotype
