from enum import Enum

from evolutionary_optimization.phenotype.abstract_phenotype import AbstractPhenotype
from evolutionary_optimization.phenotype.inverted_parabola_phenotype import InvertedParabolaPhenotype
from evolutionary_optimization.phenotype.parabola_phenotype import ParabolaPhenotype


class Phenotypes(str, Enum):
    """Enum containing implemented phenotypes."""
    PARABOLA = "parabola"
    INVERTED_PARABOLA = "inverted_parabola"

class Phenotype:
    """Maps Phenotypes to their associated concrete class based on AbstractPhenotype."""
    phenotypes_dictionary = {
        Phenotypes.PARABOLA: ParabolaPhenotype,
        Phenotypes.INVERTED_PARABOLA: InvertedParabolaPhenotype,
    }

    @classmethod
    def get_phenotype(cls, phenotypes_enum: Phenotypes) -> type(AbstractPhenotype):
        """Return class of desired AbstractPhenotype."""
        return cls.phenotypes_dictionary[phenotypes_enum]
