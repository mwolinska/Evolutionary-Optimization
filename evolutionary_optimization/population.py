
from random import shuffle
from typing import Tuple, List

from fitness_score.abstract_fitness_function import AbstractFitnessFunction
from phenotype.abstract_phenotype import AbstractPhenotype
from phenotype.parabola_phenotype import ParabolaPhenotype


class Population:
    def __init__(self,
                 number_of_individuals: int,
                 phenotype: AbstractPhenotype,
                 ):
        """Contains all individuals being evaluated.

        The Population object is used by the Evolution object to create, store and update the individuals
        being evaluated. It also performs crossover of individuals if required when updating the population.

        Args:
            number_of_individuals: number of individuals in the desired population.
            phenotype:
        """

        self.n_individuals = number_of_individuals
        self.population = self._create_population(phenotype)
        self.phenotype = phenotype
        self.best_individual = phenotype.from_phenotype(phenotype)
        self.mutation = True if phenotype.genotype.mutation_probability > 0 else False
        self.crossover = True if phenotype.genotype.mutation_probability > 0 else False

    def _create_population(self, phenotype) -> List[AbstractPhenotype]:
        """Creates initial population used to evaluate phenotype_folder.

        Returns:
            List of Individual instances of length n_individuals.
        """
        individuals = []
        for i in range(self.n_individuals):
            new_individual = phenotype.from_phenotype(phenotype)
            individuals.append(new_individual)
        return individuals

    def create_list_of_new_individuals(self, n_new_individuals: int) -> List[AbstractPhenotype]:
        """Creates a list of Individual instances.

        Args:
            n_new_individuals: number of desired individuals in list.

        Returns:
            List of Individual instances of length n_new_individuals.
        """
        new_individuals_list = []
        for i in range(n_new_individuals):
            new_individuals_list.append(self.phenotype.generate_random_phenotype())

        return new_individuals_list

    def evaluate_population(self, fitness_function: AbstractFitnessFunction):
        """Calculates fitness scores for each individual in population.

        For each individual in the population calculates the fitness score and stores the best individual
        in the population.best_individual attribute.

        Args:
            fitness_function: fitness function used to evaluate a phenotype.
        """
        for phenotype in self.population:
            if phenotype.phenotype_value is None:
                phenotype.evaluate_phenotype()
            fitness_score = fitness_function.evaluate(phenotype=phenotype)

            if self.best_individual.phenotype_value is None or \
                    fitness_score > fitness_function.evaluate(self.best_individual):

                self.best_individual = phenotype

    def update_population(self, fitness_function: AbstractFitnessFunction):
        """Updates self.all_genes following evaluation.

        Once all individuals in the population have been evaluated, the top individuals are kept (elitism),
        the remaining individuals are updated by a combination of mutation and/or crossover if these were
        defined in the Evolution instance. If neither was selected, the non-elite individuals will
        be replaced by randomly generated individuals.
        """
        elite_individuals, non_elite_individuals = self.split_elite_individuals(fitness_function)

        if self.crossover:
            non_elite_individuals = self.crossover_for_population_segment(non_elite_individuals)

        if self.mutation:
            for individual in non_elite_individuals:
                individual.mutate()

        if not self.crossover and not self.mutation:
            non_elite_individuals = self.create_list_of_new_individuals(len(non_elite_individuals))

        new_individuals_list = elite_individuals + non_elite_individuals
        self.population = new_individuals_list

    def crossover_for_population_segment(self, list_of_parents: List[AbstractPhenotype]) -> List[AbstractPhenotype]:
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
            child_1, child_2 = list_of_parents[i].crossover(list_of_parents[i + 1])
            list_of_children.append(child_1)
            list_of_children.append(child_2)

        return list_of_children

    def split_elite_individuals(self, fitness_func) -> Tuple[List[AbstractPhenotype], List[AbstractPhenotype]]:
        """Splits list of individuals into elite and non-elite individuals.

        The function will create two lists to separate out elite individuals i.e. ones with the highest fitness
        scores, from those with lower fitness scores. Top 20% of individuals (or at least 1) will be kept from
        a list. The rest will be assigned to a separate list, which will be updated using crossover and/or mutation.

        Returns:
            Tuple of List[Individual] and List[Individual].
        """
        # TODO allow user to define % of elitism

        sorted_individuals = self.sort_phenotypes_by_fitness_score(fitness_func)
        elite_individual_threshold = max(1, self.n_individuals // 5)
        elite_individuals = sorted_individuals[:elite_individual_threshold]
        non_elite_individuals = sorted_individuals[elite_individual_threshold:]
        shuffle(non_elite_individuals)
        return elite_individuals, non_elite_individuals

    def sort_phenotypes_by_fitness_score(self, fitness_function: AbstractFitnessFunction):
        phenotype_and_fitness_score_tuple_list = []
        for phenotype in self.population:
            fitness_score = fitness_function.evaluate(phenotype)
            phenotype_and_fitness_score_tuple_list.append((phenotype, fitness_score))

        sorted_phenotype_tuples = sorted(phenotype_and_fitness_score_tuple_list, key=get_score_for_sorting, reverse=True)
        sorted_phenotypes = []
        for my_tuple in sorted_phenotype_tuples:
            sorted_phenotypes.append(my_tuple[0])

        return sorted_phenotypes


def get_score_for_sorting(a_tuple: Tuple[AbstractPhenotype, int]):
    """Key for sort function used in Population object.

    Provides a key for sorting individuals using python's sort function used by the update_population function
    within the Population object.

    Args:
        individual: an Individual instance.
    Returns:
        Float equal to an individual's fitness score.
    """
    return a_tuple[1]
