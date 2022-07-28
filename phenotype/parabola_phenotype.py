from typing import Union

from genotype.binary_list_genotype import BinaryListGenotype
from genotype.integer_list_genotype import IntegerListGenotype
from phenotype.abstract_phenotype import AbstractPhenotype


class ParabolaPhenotype(AbstractPhenotype):
    def __init__(self, genotype: Union[BinaryListGenotype, IntegerListGenotype]):
        self.genotype = genotype
        self._phenotype_value = None

    @property
    def phenotype_value(self):
        return self._phenotype_value

    @phenotype_value.setter
    def phenotype_value(self, value: int):
        self._phenotype_value = value

    @classmethod
    def from_phenotype(cls, base_phenotype: "ParabolaPhenotype") -> "ParabolaPhenotype":
        new_genotype = base_phenotype.genotype.build_random_genotype(number_of_genes=base_phenotype.genotype.number_of_genes,
                                                                     value_range=base_phenotype.genotype.value_range,
                                                                     mutation_probability=base_phenotype.genotype.mutation_probability,
                                                                     ratio_of_population_for_crossover=base_phenotype.genotype.ratio_of_population_for_crossover,
                                                                    )
        return cls(new_genotype)

    def evaluate_phenotype(self):
        if isinstance(self.genotype, BinaryListGenotype):
            float_genotype = self.genotype.return_integer_form()
        else:
            float_genotype = self.genotype.genotype[0]

        phenotype = float_genotype ** 2
        self.phenotype_value = phenotype

    def crossover(self, parent_2: "ParabolaPhenotype"):
        child_genotype_1, child_genotype_2 = self.genotype.crossover(parent_2.genotype)
        child_1 = ParabolaPhenotype(child_genotype_1)
        child_2 = ParabolaPhenotype(child_genotype_2)
        return child_1, child_2

    def mutate(self):
        self.genotype.mutate()
