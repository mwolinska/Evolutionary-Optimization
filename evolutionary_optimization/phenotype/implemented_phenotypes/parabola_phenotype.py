from typing import Tuple

from evolutionary_optimization.genotype.genotype_model.abstract_genotype import AbstractGenotype
from evolutionary_optimization.genotype.implemented_genotypes.binary_list_genotype import BinaryListGenotype
from evolutionary_optimization.phenotype.phenotype_model.abstract_phenotype import AbstractPhenotype


class ParabolaPhenotype(AbstractPhenotype):
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
    def from_phenotype(cls, base_phenotype: "ParabolaPhenotype") -> "ParabolaPhenotype":
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
        if isinstance(self.genotype, BinaryListGenotype):
            float_genotype = self.genotype.return_integer_form()
        else:
            float_genotype = self.genotype.genotype[0]

        phenotype = float_genotype ** 2
        self.phenotype_value = phenotype

    def crossover(self, parent_2: "ParabolaPhenotype") -> Tuple["ParabolaPhenotype", "ParabolaPhenotype"]:
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
        child_1 = ParabolaPhenotype(child_genotype_1)
        child_2 = ParabolaPhenotype(child_genotype_2)
        return child_1, child_2

    def mutate(self):
        """In place modification of the genotype by randomly changing genes based on mutation probability.

        Calls mutate method as implemented for the genotype attribute in order to perform mutation.
        Updates genotype attribute in place.
        """
        self.genotype.mutate()
