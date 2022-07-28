from enum import Enum

from genotype.abstract_genotype import AbstractGenotype
from genotype.binary_list_genotype import BinaryListGenotype
from genotype.integer_list_genotype import IntegerListGenotype


class Genotypes(str, Enum):
    BINARY_LIST = "binary_list"
    INTEGER_LIST = "integer_list"


class Genotype:
    genotypes_dictionary = {
        Genotypes.BINARY_LIST: BinaryListGenotype,
        Genotypes.INTEGER_LIST: IntegerListGenotype,
    }

    @classmethod # TODO I'm still not sure why it's better to return class than instance
    def get_genotype(cls, genotype_enum: Genotypes) -> type(AbstractGenotype):
        return cls.genotypes_dictionary[genotype_enum]
