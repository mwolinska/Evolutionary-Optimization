import random

from typing import Optional, Tuple


class Individual:
    def __init__(self, values_range: Tuple[int, int], value: Optional[float] = None):
        self.fitness_score = None

        if value is not None:
            self.value = value
        else:
            self.value = random.uniform(values_range[0], values_range[1])


def get_score_for_sorting(individual: Individual):
    return individual.fitness_score
