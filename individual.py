import random
from typing import List, Union

import numpy as np

from genotype import Genotype, GenotypeProperties


class Individual:
    def __init__(self, genotype_properties: GenotypeProperties):
        self.genotype = Genotype(genotype_properties)
        self.genotype.mutation_probability = genotype_properties.mutation_probability
        self.fitness_score = None
