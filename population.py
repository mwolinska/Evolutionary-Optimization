from random import random, shuffle
from typing import Tuple, List
import random

from genotype import GenotypeKey, GenotypeProperties
from individual import Individual, get_score_for_sorting


class Population:
    def __init__(self,
                 n_individuals: int,
                 genotype_properties: GenotypeProperties,
                 ):
        self.n_individuals = n_individuals
        self.genotype_properties = genotype_properties
        self.individual_value_range = genotype_properties.value_range
        self.all_individuals = self._create_population()
        self.best_individual = Individual(genotype_properties)

    def _create_population(self) -> List[Individual]:
        individuals = []
        for i in range(self.n_individuals):
            new_individual = Individual(self.genotype_properties)
            individuals.append(new_individual)
        return individuals

    def add_new_individuals(self, n_new_individuals):
        for i in range(n_new_individuals):
            self.all_individuals.append(Individual(self.genotype_properties))

    def update_population(self):
        sorted_individuals = sorted(self.all_individuals, key=get_score_for_sorting, reverse=True)
        elite_individual_threshold = max(1, self.n_individuals // 5)
        new_all_individuals = sorted_individuals[:elite_individual_threshold]
        individuals_for_crossover = sorted_individuals[elite_individual_threshold:]
        shuffle(individuals_for_crossover)

        for i in range(0, len(individuals_for_crossover), 2):
            if (i+1) <= len(individuals_for_crossover) - 1:
                child_1, child_2 = self.crossover(individuals_for_crossover[i], individuals_for_crossover[i+1])

                child_1.mutation()
                child_2.mutation()

                new_all_individuals.append(child_1)
                new_all_individuals.append(child_2)

        self.all_individuals = new_all_individuals
        missing_individuals = self.n_individuals - len(self.all_individuals)

        if missing_individuals != 0:
            self.add_new_individuals(missing_individuals)
        # # n_individuals_to_crossover= self.n_individuals - 2 * elite_individual_threshold
        # # individuals_to_crossover = sorted_individuals[elite_individual_threshold:(self.n_individuals - elite_individual_threshold)]
        # for individual in sorted_individuals[elite_individual_threshold:]:
        #     individual.mutation()
        #     self.all_individuals.append(individual)
        #
        # self.all_individuals = new_all_individuals
        # self.add_new_individuals(elite_individual_threshold)

    def crossover(self, parent_1: Individual, parent_2: Individual) -> Tuple[Individual, Individual]:
        if len(parent_1.genotype.all_genes) != len(parent_2.genotype.all_genes):
            raise NameError("The Individuals have genotypes of different lengths - crossover is impossible")

        n_genes = len(parent_1.genotype.all_genes)
        if n_genes > 1:
            last_slice_index = n_genes - 1
            gene_slice_index = random.randint(1, last_slice_index)

            child_1_genotype_part_1 = parent_1.genotype[:gene_slice_index]
            child_1_genotype_part_2 = parent_2.genotype[gene_slice_index:]
            child_1_all_genes = child_1_genotype_part_1 + child_1_genotype_part_2

            child_2_genotype_part_1 = parent_2.genotype[:gene_slice_index]
            child_2_genotype_part_2 = parent_1.genotype[gene_slice_index:]
            child_2_all_genes = child_2_genotype_part_1 + child_2_genotype_part_2

            child_1 = self.create_child(child_1_all_genes)
            child_2 = self.create_child(child_2_all_genes)

        else:
            child_1 = parent_1
            child_2 = parent_2

        return child_1, child_2

    def create_child(self, new_genotype_all_genes):
        child = Individual.from_all_genes(self.genotype_properties, new_genotype_all_genes)
        return child
