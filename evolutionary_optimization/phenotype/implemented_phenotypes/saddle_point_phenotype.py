from typing import Tuple

from evolutionary_optimization.genotype.implemented_genotypes.float_list_genotype import FloatListGenotype
from evolutionary_optimization.phenotype import AbstractPhenotype

class SaddlePointPhenotype(AbstractPhenotype):
    def __init__(self, genotype: FloatListGenotype):
        """Initialise AbstractPhenotype object.

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
    def phenotype_value(self, value):
        self._phenotype_value = value

    def evaluate_phenotype(self):
        """Calculate phenotype value using genotype."""
        x = self.genotype.genotype[0]
        y = (x ** 4) - (2 * x ** 3) + 2
        self.phenotype_value = y

    def crossover(self, parent_2: "AbstractPhenotype") -> Tuple["AbstractPhenotype", "AbstractPhenotype"]:
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
        child_1 = SaddlePointPhenotype(child_genotype_1)
        child_2 = SaddlePointPhenotype(child_genotype_2)
        return child_1, child_2

    def mutate(self):
        """In place modification of the genotype by randomly changing genes based on mutation probability.

        Calls mutate method as implemented for the genotype attribute in order to perform mutation.
        Updates genotype attribute in place.
        """
        self.genotype.mutate()

    @classmethod
    def from_phenotype(cls, base_phenotype: "AbstractPhenotype"):
        """Create new phenotype with the same attributes as the base phenotype."""
        new_genotype = base_phenotype.genotype.build_random_genotype(
            number_of_genes=base_phenotype.genotype.number_of_genes,
            value_range=base_phenotype.genotype.value_range,
            mutation_probability=base_phenotype.genotype.mutation_probability,
            ratio_of_population_for_crossover=base_phenotype.genotype.ratio_of_population_for_crossover,
        )
        return cls(new_genotype)
