import abc
from enum import Enum
from abc import ABC, abstractmethod

from genotype.genotype import Genotype


class AbstractPhenotype(ABC):

    @abstractmethod
    def function_to_optimise(self, genotype: Genotype):
        pass
