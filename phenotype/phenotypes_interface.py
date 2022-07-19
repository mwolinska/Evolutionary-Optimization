from enum import Enum

from phenotype.abstract_phenotype import AbstractPhenotype
from phenotype.mse import MSE
from phenotype.test_phenotype import TestPhenotype


class Phenotypes(str, Enum):
    MSE = "mse"
    TEST = "test"

    @staticmethod
    def get_phenotype(phenotype: "Phenotypes") -> AbstractPhenotype:
        if phenotype == Phenotypes.MSE:
            return MSE()
        elif phenotype == Phenotypes.TEST:
            return TestPhenotype()
