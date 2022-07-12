from typing import Tuple, List

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
        self.all_individuals = sorted_individuals[:elite_individual_threshold]
        self.add_new_individuals(n_individuals_to_replace)
        for individual in sorted_individuals[elite_individual_threshold:]:
            individual.mutation()
            self.all_individuals.append(individual)
