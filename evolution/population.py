import random
from random import random, shuffle
from typing import Tuple, List

from evolution.individual import Individual, get_score_for_sorting
from genotype.genotype_data_model import GenotypeProperties, GenotypeKey
from phenotype.phenotypes_interface import Phenotypes


class Population:
    def __init__(self,
                 n_individuals: int,
                 genotype_properties: GenotypeProperties,
                 phenotype: Phenotypes,
                 crossover: bool = False
                 ):
        """Contains all individuals being evaluated.

        The Population object is used by the Evolution object to create, store and update the individuals
        being evaluated. It also performs crossover of individuals if required when updating the population.

        Args:
            n_individuals: number of individuals in the desired population.
            genotype_properties: all properties required to build an individual.
                As defined by the instance of the Evolution object.
            crossover: whether crossover should happen when updating the population.
        """

        self.n_individuals = n_individuals
        self.genotype_properties = genotype_properties
        self.phenotype = phenotype
        self.all_individuals = self._create_population()
        self.best_individual = Individual(genotype_properties, phenotype)
        self.crossover = crossover
        self.mutation = True if genotype_properties.mutation_probability > 0 else False

    def _create_population(self) -> List[Individual]:
        """Creates initial population used to evaluate phenotype.

        Returns:
            List of Individual instances of length n_individuals.
        """
        individuals = []
        for i in range(self.n_individuals):
            new_individual = Individual(self.genotype_properties, self.phenotype)
            individuals.append(new_individual)
        return individuals

    def create_list_of_new_individuals(self, n_new_individuals: int) -> List[Individual]:
        """Creates a list of Individual instances.

        Args:
            n_new_individuals: number of desired individuals in list.

        Returns:
            List of Individual instances of length n_new_individuals.
        """
        new_individuals_list = []
        for i in range(n_new_individuals):
            new_individuals_list.append(Individual(self.genotype_properties, self.phenotype))

        return new_individuals_list

    def update_population(self):
        """Updates self.all_genes following evaluation.

        Once all individuals in the population have been evaluated, the top individuals are kept (elitism),
        the remaining individuals are updated by a combination of mutation and/or crossover if these were
        defined in the Evolution instance. If neither was selected, the non-elite individuals will
        be replaced by randomly generated individuals.
        """

        elite_individuals, non_elite_individuals = self.split_elite_individuals()
        if self.crossover:
            non_elite_individuals = self.crossover_for_list(non_elite_individuals)

        if self.mutation:
            for individual in non_elite_individuals:
                individual.mutation()

        if not self.crossover and not self.mutation:
            non_elite_individuals = self.create_list_of_new_individuals(len(non_elite_individuals))

        new_individuals_list = elite_individuals + non_elite_individuals
        self.all_individuals = new_individuals_list

    def crossover_for_list(self, list_of_parents: List[Individual]) -> List[Individual]:
        """Crossover method for a genotype of type list.

        This method creates a new list of individuals (children) based on the parents' genotypes.

        Args:
            list_of_parents: list of individuals which should be used to generate offspring.

        Returns:
            List of Individual.
        """
        list_of_children = []

        if len(list_of_parents) % 2 != 0:
            list_of_children.append(list_of_parents[-1])
            list_of_parents.pop(-1)

        for i in range(0, len(list_of_parents), 2):
            child_1, child_2 = self.single_point_crossover(list_of_parents[i], list_of_parents[i + 1])
            list_of_children.append(child_1)
            list_of_children.append(child_2)

        return list_of_children

    def single_point_crossover(self, parent_1: Individual, parent_2: Individual) -> Tuple[Individual, Individual]:
        """Performs single point crossover operation for 1 set of parents.

        A random integer is generated to split the genotype of the two individuals -
        this is the gene slice index. Then two child Individuals are generated with the complementary parts
        of the parent individuals. If the parent's genotype length is 1, cross over is impossible so the parent
        instances are returned.

        Example:
            parent_1.genotype.all_genes = [1, 2, 3, 4]
            parent_2.genotype.all_genes = [A, B, C, D]
            gene_slice_index = 1

            child_1.genotype.all_genes = [1, B, C, D]
            child_2.genotype.all_genes = [A, 2, 3, 4]

        Args:
            parent_1: Individual which will be used to create an offspring.
            parent_2: Individual which will be used to create an offspring.

        Returns:
            Tuple of Individual.
        """
        if len(parent_1.genotype.genotype) != len(parent_2.genotype.genotype):
            raise NameError("The Individuals have genotypes of different lengths - crossover is impossible")

        if self.genotype_properties.n_genes == 1:
            return parent_1, parent_2
        else:
            last_slice_index = self.genotype_properties.n_genes - 1
            gene_slice_index = random.randint(1, last_slice_index)

            if self.genotype_properties.genotype_key == GenotypeKey.LIST:
                child_1 = self.single_point_crossover_for_list(parent_1, parent_2, gene_slice_index)
                child_2 = self.single_point_crossover_for_list(parent_2, parent_1, gene_slice_index)

            else:
                raise NotImplementedError

            return child_1, child_2

    def single_point_crossover_for_list(self, parent_1: Individual, parent_2: Individual, gene_slice_index: int) -> Individual:
        """A single point crossover for genotype of type list.

        This is a single point crossover. Using the gene_slice_index, for both parents the genotype.all genes are sliced.
        The slice [:gene_slice_index[ is taken from parent_1 and the slice [gene_slice_index:] is taken from parent_2.
        The two complementary slices are then joined to create a new individual (a child) from the new genotype.

        Args:
            parent_1: Individual which will be used to create an offspring.
            parent_2: Individual which will be used to create an offspring.
            gene_slice_index: random integer at which the parent genotypes will be sliced.

        Returns:
            An Individual instance.
        """
        child_genotype_part_1 = parent_1.genotype.genotype[:gene_slice_index]
        child_genotype_part_2 = parent_2.genotype.genotype[gene_slice_index:]
        child_all_genes = child_genotype_part_1 + child_genotype_part_2
        child = Individual.from_genotype(self.genotype_properties, child_all_genes)
        return child

    def split_elite_individuals(self) -> Tuple[List[Individual], List[Individual]]:
        """Splits list of individuals into elite and non-elite individuals.

        The function will create two lists to separate out elite individuals i.e. ones with the highest fitness
        scores, from those with lower fitness scores. Top 20% of individuals (or at least 1) will be kept from
        a list. The rest will be assigned to a separate list, which will be updated using crossover and/or mutation.

        Returns:
            Tuple of List[Individual] and List[Individual].
        """
        # TODO allow user to define % of elitism
        sorted_individuals = sorted(self.all_individuals, key=get_score_for_sorting, reverse=True)
        elite_individual_threshold = max(1, self.n_individuals // 5)
        elite_individuals = sorted_individuals[:elite_individual_threshold]
        non_elite_individuals = sorted_individuals[elite_individual_threshold:]
        shuffle(non_elite_individuals)
        return elite_individuals, non_elite_individuals
