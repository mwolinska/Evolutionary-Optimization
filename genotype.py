import random
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Optional

import numpy as np

class GenotypeKey(str, Enum):
    a_list = "list"
    a_string = "str"

@dataclass
class GenotypeProperties:
    genotype_key: GenotypeKey
    n_genes: int
    value_range: Tuple[int, int]
    mutation_probability: float

class Genotype:
    def __init__(self, genotype_properties: GenotypeProperties):
        self.all_genes = self.build_genotype(genotype_properties)
        self.genotype_key = genotype_properties.genotype_key
        self.value_range = genotype_properties.value_range
        self.mutation_probability = genotype_properties.mutation_probability



    @staticmethod
    def build_genotype(genotype_properties: GenotypeProperties):
        all_genes = None
        if genotype_properties.genotype_key == "list":
            all_genes = []
            for i in range(genotype_properties.n_genes):
                new_gene = random.randint(genotype_properties.value_range[0], genotype_properties.value_range[1])
                all_genes.append(new_gene)
                print(all_genes)

        return all_genes

class Gene:
    def __init__(self, a_gene):
        self.gene_type = type(a_gene)

if __name__ == '__main__':
    test = Genotype.a_list
    print()
