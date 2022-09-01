from typing import Tuple

import numpy as np

from evolutionary_optimization.genotype.genotype_model.abstract_genotype import AbstractGenotype
from evolutionary_optimization.phenotype.phenotype_model.abstract_phenotype import AbstractPhenotype

class BoothPhenotype(AbstractPhenotype):
    # TODO (Marta): Import of abstract phenotype doesn't work
    def __init__(self, genotype: AbstractGenotype): # Union[BinaryListGenotype, IntegerListGenotype]
        """Initialise InvertedParabolaPhenotype object.

        Args
            genotype: an AbstractGenotype that defines the phenotype.
        """
        self._genotype = genotype
        self._phenotype_value = None

    @property
    def genotype(self):
        return self._genotype

    @genotype.setter
    def genotype(self, value):
        self._genotype = value

    @property
    def phenotype_value(self):
        """Stores value of the phenotype based on the genotype - calculated using evaluate_phenotype."""
        return self._phenotype_value

    @phenotype_value.setter
    def phenotype_value(self, value: int):
        """Setter for phenotype_value property."""
        self._phenotype_value = value

    @classmethod
    def from_phenotype(cls, base_phenotype: "BoothPhenotype") -> "BoothPhenotype":
        """Create new phenotype with the same attributes as the base phenotype, but a new random genotype.genotype."""
        new_genotype = base_phenotype.genotype.build_random_genotype(
            number_of_genes=base_phenotype.genotype.number_of_genes,
            value_range=base_phenotype.genotype.value_range,
            mutation_probability=base_phenotype.genotype.mutation_probability,
            ratio_of_population_for_crossover=base_phenotype.genotype.ratio_of_population_for_crossover,
        )
        return cls(new_genotype)

    def evaluate_phenotype(self):
        """In place method to calculate phenotype value using genotype.

        This phenotype follows x^2 and as such is a single parameter optimisation problem.
        For a binary genotype the integer value is returned,for an integer list genotype only the first value is used.
        It updates the phenotype_value property in place once the calculation is done.
        """

        x_1 = self.genotype.genotype[0]
        x_2 = self.genotype.genotype[1]

        phenotype = (x_1 + x_2 - 7) ** 2 + (2 * x_1 + x_2 - 5) ** 2
        self.phenotype_value = phenotype

    @staticmethod
    def evaluate_phenotype_using_arrays(x_values: np.ndarray, y_values: np.ndarray) -> np.ndarray:
        return (x_values + y_values - 7) ** 2 + (2 * x_values + y_values - 5) ** 2

    def crossover(self, parent_2: "BoothPhenotype") -> Tuple["BoothPhenotype", "BoothPhenotype"]:
        """Perform crossover between two phenotypes.

        Calls crossover method from the genotype attribute. Combines a portion of this object's genotype
        with that of parent_2 to return 2 new phenotypes based on the combined genotypes.
        The new genotype length is the same as of the parents.

        Args:
            parent_2: a phenotype of the same class whose genotype will be mixed with

        Returns:
            Two new phenotype instances based on the combined genotypes of the two parents.
        """
        child_genotype_1, child_genotype_2 = self.genotype.crossover(parent_2.genotype)
        child_1 = BoothPhenotype(child_genotype_1)
        child_2 = BoothPhenotype(child_genotype_2)
        return child_1, child_2

    def mutate(self):
        """In place modification of the genotype by randomly changing genes based on mutation probability.

        Calls mutate method as implemented for the genotype attribute in order to perform mutation.
        Updates genotype attribute in place.
        """
        self.genotype.mutate()
