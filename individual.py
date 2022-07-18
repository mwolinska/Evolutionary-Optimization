from genotype import Genotype, GenotypeProperties, GenotypeKey


class Individual:
    def __init__(self, genotype_properties: GenotypeProperties):
        """An object containing all information of one instance being evaluated.

        An individual is effectively an instance being evaluated during the evolution. An individual contains
        a genotype and a fitness score (updated upon evaluation during Evolution).

        Args:
            genotype_properties: all genotype properties as required for an individual.
        """
        self.genotype = Genotype(genotype_properties)
        # TODO the line below is obsolete? Check
        self.genotype.mutation_probability = genotype_properties.mutation_probability
        self.fitness_score = None

    @classmethod
    def from_all_genes(cls, genotype_properties: GenotypeProperties, new_all_genes):
        """Creates an individual from a set of genes.

        An individual is created, but instead of a random set of genes the new_all_genes argument
        is used to populate the individual.all_genes attribute.

            genotype_properties: all genotype properties as required for an individual.
            new_all_genes: an instance of all_genes in alignment with the GenotypeKey defined by genotype_properties.
        Returns:
            An Individual object with the genotype properties passed in the function except for
                individual.all_genes which contain the new_all_genes information.
        """
        return new_individual

    def mutation(self):
        """Performs mutation of the individual.

        The genotype attribute is updated through a mutation in line with the function definition within the
        Genotype class.
        """
        new_genotype = self.genotype.mutate()
        self.genotype.genotype = new_genotype

def get_score_for_sorting(individual: Individual):
    """Key for sort function used in Population object.

    Provides a key for sorting individuals using python's sort function used by the update_population function
    within the Population object.

    Args:
        individual: an Individual instance.
    Returns:
        Float equal to an individual's fitness score.
    """
    return individual.fitness_score

if __name__ == '__main__':
    gen_prop = GenotypeProperties(
        genotype_key=GenotypeKey.a_list,
        n_genes=1,
        value_range=(0,1), mutation_probability=1)
    test_indiv = Individual.from_all_genes(gen_prop, [1])
    print(test_indiv.genotype.all_genes)
    # a_individual = Individual([1, 1, 1, 1, 1], mutation_probability=1)
    # b_individual = Individual([2, 2, 2, 2, 2], mutation_probability=1)
    # # a_individual.mutate()
    # # print(a_individual.genotype)
    #
    # c_individual = test.crossover(a_individual, b_individual)
    # print(c_individual.genotype)
