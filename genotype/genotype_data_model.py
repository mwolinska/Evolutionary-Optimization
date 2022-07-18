from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class GenotypeKey(str, Enum):
    """Class to define allowed types of genotypes.

    This key will then be used to define methods used throughout the package e.g. a different mutation
    would be used for a_list as opposed to a_string.
    """
    # TODO how do you properly write an enum docstring?
    LIST = "list"
    STRING = "str"


class Gene(str, Enum):
    INTEGER = "int"
    STRING = "str"
    BINARY = "binary"
    FLOAT = "float"


@dataclass
class GenotypeProperties:
    """Object containing all information required to build a genotype.

    Attributes:
        genotype_key: defines the type of genotype.
        n_genes: number of genes required in a genotype.
        value_range: tuple of minimum and maximum values for a gene.
        mutation_probability: probability of a gene mutating in one generation.
    """
    genotype_key: GenotypeKey
    n_genes: int
    value_range: Tuple[int, int]
    mutation_probability: float
