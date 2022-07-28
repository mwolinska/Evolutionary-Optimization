from abc import ABC, abstractmethod
from typing import Tuple, Optional


class AbstractGenotype(ABC):
    @abstractmethod
    def __init__(
        self,
        genotype,
        mutation_probability: float,
        ratio_of_population_for_crossover: float,
        number_of_genes: int,
        value_range: Tuple[int, int],
    ):
        pass

    @classmethod
    @abstractmethod
    def build_random_genotype(
        cls,
        mutation_probability: Optional[float],
        ratio_of_population_for_crossover: Optional[float]
    ) -> "AbstractGenotype":
        pass

    @abstractmethod
    def mutate(self):
        pass

    @abstractmethod
    def crossover(self,
        parent_2: "AbstractGenotype",
    ) -> Tuple:

        pass
