from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class GenotypeKey(Enum):
    """Class to define allowed types of genotypes.

    This key will then be used to define methods used throughout the package e.g. a different mutation
    would be used for a_list as opposed to a_string.
    """
    # TODO how do you properly write an enum docstring?
    LIST = list
    STRING = str


class Gene(Enum):
    INTEGER = int
    STRING = str
    BINARY = bin
    FLOAT = float


@dataclass
class GenotypeProperties:
    """Object containing all information required to build a genotype.

    Attributes:
        genotype_key: defines the type of genotype.
        type_of_gene: defines the type of one gene.
        n_genes: number of genes required in a genotype.
        value_range: tuple of minimum and maximum values for a gene.
        mutation_probability: probability of a gene mutating in one generation.
    """
    genotype_key: type
    type_of_gene: type
    n_genes: int
    value_range: Tuple[int, int]
    mutation_probability: float

if __name__ == '__main__':
    test = GenotypeProperties(list, str, 3, (0, 2), 1)
    my_key = GenotypeKey(test.genotype_key)
    print(my_key)
