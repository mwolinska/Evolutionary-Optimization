import random
from typing import List, Union

import numpy as np

from genotype import Genotype, GenotypeProperties, GenotypeKey


class Individual:
    def __init__(self, genotype_properties: GenotypeProperties):
        self.genotype = Genotype(genotype_properties)
        self.genotype.mutation_probability = genotype_properties.mutation_probability
        self.fitness_score = None

    @classmethod
    def from_all_genes(cls, genotype_poroperties, new_all_genes):
        """Creates an individual from a set of genes.
        new_individual.genotype.all_genes = new_all_genes
        return new_individual

    def mutation(self):
        new_genotype = self.genotype.mutate()
        self.genotype.genotype = new_genotype

if __name__ == '__main__':
    gen_prop = GenotypeProperties(
        genotype_key=GenotypeKey.a_list,
        n_genes=1,
        value_range=(0,1), mutation_probability=1)
    test_indiv = Individual.from_all_genes(gen_prop, [1])
    print(test_indiv.genotype.all_genes)
    # a_individual = Individual([1, 1, 1, 1, 1], mutation_probability=1)
    # b_individual = Individual([2, 2, 2, 2, 2], mutation_probability=1)
    # # a_individual.mutate()
    # # print(a_individual.genotype)
    #
    # c_individual = test.crossover(a_individual, b_individual)
    # print(c_individual.genotype)


def get_score_for_sorting(individual: Individual):
    return individual.fitness_score
