from enum import Enum

from evolutionary_optimization.genotype.genotype_model.abstract_genotype import AbstractGenotype
from evolutionary_optimization.genotype import BinaryListGenotype
from evolutionary_optimization.genotype import IntegerListGenotype
from evolutionary_optimization.genotype.implemented_genotypes.float_list_genotype import FloatListGenotype


class Genotypes(str, Enum):
    """Enum containing implemented genotypes."""
    BINARY_LIST = "binary_list"
    INTEGER_LIST = "integer_list"
    FLOAT_LIST = "float_list"


class Genotype:
    """Maps Genotypes to their associated concrete class based on AbstractGenotype."""
    genotypes_dictionary = {
        Genotypes.BINARY_LIST: BinaryListGenotype,
        Genotypes.INTEGER_LIST: IntegerListGenotype,
        Genotypes.FLOAT_LIST: FloatListGenotype
    }

    @classmethod
    def get_genotype(cls, genotype_enum: Genotypes) -> type(AbstractGenotype):
        """Return class of desired AbstractGenotype."""
        return cls.genotypes_dictionary[genotype_enum]
