from enum import Enum

from phenotype.abstract_phenotype import AbstractPhenotype
from phenotype.inverted_parabola_phenotype import InvertedParabolaPhenotype
from phenotype.parabola_phenotype import ParabolaPhenotype


class Phenotypes(str, Enum):
    PARABOLA = "parabola"
    INVERTED_PARABOLA = "inverted_parabola"

class Phenotype:
    phenotypes_dictionary = {
        Phenotypes.PARABOLA: ParabolaPhenotype,
        Phenotypes.INVERTED_PARABOLA: InvertedParabolaPhenotype,
    }

    @classmethod
    def get_phenotype(cls, phenotypes_enum: Phenotypes) -> type(AbstractPhenotype):
        return cls.phenotypes_dictionary[phenotypes_enum]
