from typing import Tuple

from individual import Individual


class Population:
    def __init__(self, n_individuals, individual_value_range: Tuple[int, int] = (0, 1)):
        self.n_individuals = n_individuals
        self.individual_value_range = individual_value_range
        self.all_individuals = self._create_population()
        self.best_individual = Individual(individual_value_range)

    def _create_population(self):
        individuals = []
        for i in range(self.n_individuals):
            new_individual = Individual(self.individual_value_range)
            individuals.append(new_individual)
        return individuals

    def add_new_individuals(self, n_new_individuals):
        for i in range(n_new_individuals):
            self.all_individuals.append(Individual(self.individual_value_range))
