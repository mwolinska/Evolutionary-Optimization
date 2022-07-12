import random
from typing import List, Union

import numpy as np

from genotype import Genotype, GenotypeProperties


class Individual:
    def __init__(self, genotype_properties: GenotypeProperties):
        self.genotype = Genotype(genotype_properties)
        self.genotype.mutation_probability = genotype_properties.mutation_probability
        self.fitness_score = None

    def mutation(self):
        new_genotype = self.genotype.mutate()
        self.genotype.all_genes = new_genotype

    def crossover(self, parent_2: "Individual") -> "Individual":

        if len(self.genotype.all_genes) != len(parent_2.genotype.all_genes):
            raise NameError("The Individuals have genotypes of different lengths - crossover is impossible")

        n_genes = len(self.genotype.all_genes)
        last_slice_index = n_genes - 1
        gene_slice_index = random.randint(1, last_slice_index)
        new_genotype_part_1 = self.genotype[:gene_slice_index]
        new_genotype_part_2 = parent_2.genotype[gene_slice_index:]
        new_individual_genotype = new_genotype_part_1 + new_genotype_part_2

        new_individual = Individual(new_individual_genotype, mutation_probability=self.mutation_probability)

        return new_individual

if __name__ == '__main__':
    test = Individual([1, 1])
    a_individual = Individual([1, 1, 1, 1, 1], mutation_probability=1)
    b_individual = Individual([2, 2, 2, 2, 2], mutation_probability=1)
    # a_individual.mutate()
    # print(a_individual.genotype)

    c_individual = test.crossover(a_individual, b_individual)
    print(c_individual.genotype)


def get_score_for_sorting(individual: Individual):
    return individual.fitness_score
