from random import random, shuffle
from typing import Tuple, List
import random

from genotype import GenotypeKey, GenotypeProperties
from individual import Individual, get_score_for_sorting


class Population:
    def __init__(self,
                 n_individuals: int,
                 genotype_properties: GenotypeProperties,
                 crossover: bool = False
                 ):
        self.n_individuals = n_individuals
        self.genotype_properties = genotype_properties
        self.individual_value_range = genotype_properties.value_range
        self.all_individuals = self._create_population()
        self.best_individual = Individual(genotype_properties)
        self.crossover = crossover
        self.mutation = True if genotype_properties.mutation_probability > 0 else False

    def _create_population(self) -> List[Individual]:
        individuals = []
        for i in range(self.n_individuals):
            new_individual = Individual(self.genotype_properties)
            individuals.append(new_individual)
        return individuals

    def add_new_individuals(self, n_new_individuals) -> List[Individual]:
        new_individuals_list = []
        for i in range(n_new_individuals):
            new_individuals_list.append(Individual(self.genotype_properties))

        return new_individuals_list

    def update_population(self):
        elite_individuals, non_elite_individuals = self.split_elite_individuals()
        if self.crossover:
            non_elite_individuals = self.crossover_for_list(non_elite_individuals)

        if self.mutation:
            for individual in non_elite_individuals:
                individual.mutation()

        if not self.crossover and not self.mutation:
            non_elite_individuals = self.add_new_individuals(len(non_elite_individuals))

        new_individuals_list = elite_individuals + non_elite_individuals

        # for debugging
        for i in new_individuals_list:
            print(i.genotype.all_genes)

        self.all_individuals = new_individuals_list

    def crossover_for_list(self, list_of_parents: List[Individual]) -> List[Individual]:
        list_of_children = []

        if len(list_of_parents) % 2 != 0:
            list_of_children.append(list_of_parents[-1])
            list_of_parents.pop(-1)

        for i in range(0, len(list_of_parents), 2):
            child_1, child_2 = self.perform_crossover(list_of_parents[i], list_of_parents[i + 1])
            list_of_children.append(child_1)
            list_of_children.append(child_2)

        return list_of_children

    def perform_crossover(self, parent_1: Individual, parent_2: Individual) -> Tuple[Individual, Individual]:
        if len(parent_1.genotype.all_genes) != len(parent_2.genotype.all_genes):
            raise NameError("The Individuals have genotypes of different lengths - crossover is impossible")

        if self.genotype_properties.n_genes == 1:
            return parent_1, parent_2
        else:
            last_slice_index = self.genotype_properties.n_genes - 1
            gene_slice_index = random.randint(1, last_slice_index)

            if self.genotype_properties.genotype_key == GenotypeKey.a_list:
                child_1 = self.single_point_crossover_for_list(parent_1, parent_2, gene_slice_index)
                child_2 = self.single_point_crossover_for_list(parent_2, parent_1, gene_slice_index)

            else:
                raise NotImplementedError

            return child_1, child_2

    def single_point_crossover_for_list(self, parent_1: Individual, parent_2: Individual, gene_slice_index: int) -> Individual:
        child_genotype_part_1 = parent_1.genotype.all_genes[:gene_slice_index]
        child_genotype_part_2 = parent_2.genotype.all_genes[gene_slice_index:]
        child_all_genes = child_genotype_part_1 + child_genotype_part_2
        child = Individual.from_all_genes(self.genotype_properties, child_all_genes)
        return child

    def split_elite_individuals(self) -> Tuple[List[Individual], List[Individual]]:
        sorted_individuals = sorted(self.all_individuals, key=get_score_for_sorting, reverse=True)
        elite_individual_threshold = max(1, self.n_individuals // 5)
        elite_individuals = sorted_individuals[:elite_individual_threshold]
        non_elite_individuals = sorted_individuals[elite_individual_threshold:]
        shuffle(non_elite_individuals)
        return elite_individuals, non_elite_individuals
