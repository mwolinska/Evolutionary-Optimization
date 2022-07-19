from typing import List

from phenotype.abstract_phenotype import AbstractPhenotype


class TestPhenotype(AbstractPhenotype):
    def function_to_optimise(self, genotype: List[int]):
        y = genotype[0] ** 2 * (-1)
        # x = x[0]
        # y = -1 * x * (x - 1) * (x - 2) * (x - 3) * (x - 4)
        return y
