from enum import Enum

from evolutionary_optimization.genotype.abstract_genotype import AbstractGenotype
from evolutionary_optimization.genotype import BinaryListGenotype
from evolutionary_optimization.genotype import IntegerListGenotype


class Genotypes(str, Enum):
    """Enum containing implemented genotypes."""
    BINARY_LIST = "binary_list"
    INTEGER_LIST = "integer_list"


class Genotype:
    """Maps Genotypes to their associated concrete class based on AbstractGenotype."""
    genotypes_dictionary = {
        Genotypes.BINARY_LIST: BinaryListGenotype,
        Genotypes.INTEGER_LIST: IntegerListGenotype,
    }

    @classmethod
    def get_genotype(cls, genotype_enum: Genotypes) -> type(AbstractGenotype):
        """Return class of desired AbstractGenotype."""
        return cls.genotypes_dictionary[genotype_enum]
