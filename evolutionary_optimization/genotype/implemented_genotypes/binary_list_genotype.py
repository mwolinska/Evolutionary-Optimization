from random import randint
from typing import Tuple, Optional, List

import numpy as np

from evolutionary_optimization.genotype.genotype_model.abstract_genotype import AbstractGenotype
from evolutionary_optimization.genotype.genotype_model.genotype_utils import single_point_crossover


class BinaryListGenotype(AbstractGenotype):
    def __init__(
        self,
        genotype: Optional[List[int]] = None,
        mutation_probability: float = 0.5,
        ratio_of_population_for_crossover: float = 0.5,
        number_of_genes: int = 32,
        value_range: Tuple[int, int] = (0, 1),
    ):
        """Initialise instance of AbstractGenotype.

        Args:
            genotype: genotype used for mutation, crossover and to calculate phenotype_value.
            mutation_probability: probability of a gene mutating.
            ratio_of_population_for_crossover: ratio of population used for crossover when updating population.
            number_of_genes: number of genes in the genotype.
            value_range: minimum and maximum values of a gene.
        """
        self._genotype = genotype
        self.mutation_probability = mutation_probability
        self.ratio_of_population_for_crossover = ratio_of_population_for_crossover
        self.number_of_genes = number_of_genes
        self.value_range = value_range

    @property
    def genotype(self):
        return self._genotype

    @genotype.setter
    def genotype(self, value):
        self._genotype = value

    @classmethod
    def build_random_genotype(
        cls,
        number_of_genes: int = 32,
        value_range: Tuple[int, int] = (0, 1),
        mutation_probability: Optional[float] = 0.1,
        ratio_of_population_for_crossover: Optional[float] = 0.5
    ) -> "BinaryListGenotype":
        """Builds random genotype attribute based on requirements.

        Args:
            number_of_genes: number of genes in the genotype.
            value_range: minimum and maximum values of a gene.
            mutation_probability: probability of a gene mutating.
            ratio_of_population_for_crossover: ratio of population used for crossover when updating population.

        Returns:
              Genotype object with updated genotype attribute.
        """
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
        """In place modification of the genotype by randomly changing genes based on mutation probability."""
        new_genotype = []

        for gene in self.genotype:
            mutation = np.random.choice([True, False], p=[self.mutation_probability, 1 - self.mutation_probability])

            if mutation:
                my_list = [1, 0]
                new_gene = my_list[gene]
            else:
                new_gene = gene

            new_genotype.append(new_gene)

        self.genotype = new_genotype

    def crossover(
        self,
        parent_2_genotype: "BinaryListGenotype",
    ) -> Tuple["BinaryListGenotype", "BinaryListGenotype"]:
        """Performs single point crossover operation for 1 set of parents.

        A random integer is generated to split the genotype of the two individuals -
        this is the gene slice index. Then two child genotypes are generated with the complementary parts
        of the parent genotypes. If the parent's genotype length is 1, crossover is impossible so the parent
        instances are returned.

        Example:
            parent_1.genotype = [1, 2, 3, 4]
            parent_2.genotype = [A, B, C, D]
            gene_slice_index = 1

            child_1.genotype = [1, B, C, D]
            child_2.genotype = [A, 2, 3, 4]

        Args:
            parent_2_genotype: Individual which will be used to create an offspring.

        Returns:
            Tuple of AbstractGenotype, representing two children genotypes that are a combination of the parents.

        Todo:
            * (Marta): implement method to return Genotype copy with updated genotype attribute
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

            child_1 = BinaryListGenotype(
                genotype=child_1_genotype,
                mutation_probability=self.mutation_probability,
                ratio_of_population_for_crossover=self.ratio_of_population_for_crossover,
                number_of_genes=self.number_of_genes,
                value_range=self.value_range,
            )

            child_2 = BinaryListGenotype(
                genotype=child_2_genotype,
                mutation_probability=self.mutation_probability,
                ratio_of_population_for_crossover=self.ratio_of_population_for_crossover,
                number_of_genes=self.number_of_genes,
                value_range=self.value_range,
            )

            return child_1, child_2

    def return_integer_form(self):
        """Return integer form of a binary number."""
        power_of_2 = 0
        integer_form = 0

        for i in range(len(self.genotype) - 1, -1, -1):
            integer_form += self.genotype[i] * 2 ** power_of_2
            power_of_2 += 1
        return integer_form
