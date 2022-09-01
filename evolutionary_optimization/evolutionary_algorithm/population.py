import copy
from copy import deepcopy
from random import shuffle
from typing import Tuple, List, Union

from evolutionary_optimization.fitness_functions.abstract_fitness_function import AbstractFitnessFunction
from evolutionary_optimization.phenotype.phenotype_model.abstract_phenotype import AbstractPhenotype


class Population:
    def __init__(
        self,
        number_of_individuals: int,
        phenotype: AbstractPhenotype,
        ratio_of_elite_individuals: float,
    ):
        """Create and store phenotypes used in the Evolution object.

        The Population object is used by the Evolution object to create, store, evaluate and update phenotypes.

        Args:
            number_of_individuals: number of phenotype instances i.e. individuals in the desired population.
            phenotype: a phenotype instance with the desired genotype.
            ratio_of_elite_individuals: proportion of best scoring phenotypes in population that will be kept
                to the next generation.
        """

        self.number_of_individuals = number_of_individuals
        self.phenotype = phenotype
        self.population = self._create_population()
        self.best_individual = phenotype.from_phenotype(phenotype)
        self.mutation = True if phenotype.genotype.mutation_probability > 0 else False
        self.crossover = True if phenotype.genotype.mutation_probability > 0 else False
        self.ratio_of_elite_individuals = ratio_of_elite_individuals

    def _create_population(self) -> List[AbstractPhenotype]:
        """Create initial population of individuals.

        Returns:
            List of AbstractPhenotype instances of length number_of_individuals used in Evolution.
        """
        individuals = []
        for i in range(self.number_of_individuals):
            new_individual = self.phenotype.from_phenotype(self.phenotype)
            individuals.append(new_individual)
        return individuals

    def create_list_of_new_individuals(self, n_new_individuals: int) -> List[AbstractPhenotype]:
        """Create a list of Individual instances.

        Args:
            n_new_individuals: number of desired individuals in list.

        Returns:
            List of random Phenotype instances of length n_new_individuals.
        """
        new_individuals_list = []
        for i in range(n_new_individuals):
            new_individuals_list.append(self.phenotype.from_phenotype(self.phenotype))

        return new_individuals_list

    def evaluate_population(self, fitness_function: AbstractFitnessFunction):
        """Find best_individual in population by calculating fitness scores for all individuals.

        For each individual in the population calculates the fitness score and stores the best individual
        in the population.best_individual attribute.

        Args:
            fitness_function: fitness function used to evaluate the phenotype.
        """
        for individual in self.population:
            individual.evaluate_phenotype()
            fitness_score = fitness_function.evaluate(phenotype=individual)

            if self.best_individual.phenotype_value is None or \
                    fitness_score > fitness_function.evaluate(self.best_individual):

                self.best_individual = copy.deepcopy(individual)

    def update_population(self, fitness_function: AbstractFitnessFunction):
        """Update population attribute following evaluation.

        Once all individuals in the population have been evaluated, the top individuals are kept (elitism),
        the remaining individuals are updated by a combination of mutation and/or crossover if these were
        defined in the Evolution instance. If neither was selected, the non-elite individuals will
        be replaced by randomly generated individuals.

        Args:
            fitness_function: fitness function used to evaluate the phenotype.
        """
        elite_individuals, non_elite_individuals = self.split_elite_individuals(fitness_function)

        non_elite_individuals = non_elite_individuals[len(elite_individuals):] + deepcopy(elite_individuals)
        if self.crossover:
            number_of_individuals_for_crossover = int(self.phenotype.genotype.ratio_of_population_for_crossover
                                                      * self.number_of_individuals)
            non_elite_individuals = \
                self.crossover_for_population_segment(non_elite_individuals[:number_of_individuals_for_crossover]) + \
                non_elite_individuals[number_of_individuals_for_crossover:]

        if self.mutation:
            for individual in non_elite_individuals:
                individual.mutate()

        # TODO (Marta): This is a deviation from the standard algorithm
        # if not self.crossover and not self.mutation:
        #     non_elite_individuals = self.create_list_of_new_individuals(len(non_elite_individuals))

        new_individuals_list = elite_individuals + non_elite_individuals
        self.population = new_individuals_list

    @staticmethod
    def crossover_for_population_segment(list_of_parents: List[AbstractPhenotype]) -> List[AbstractPhenotype]:
        """Perform crossover for a list of phenotypes.

        This method creates a new list of phenotypes (children) based on the parents' genotypes by calling the
        phenotype's crossover method.

        Args:
            list_of_parents: list of phenotypes which should be used to generate offspring.

        Returns:
            List of new Phenotype objects created from their parents' genotypes.
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

    def split_elite_individuals(self, fitness_function: AbstractFitnessFunction) \
            -> Tuple[List[AbstractPhenotype], List[AbstractPhenotype]]:
        """Split list of individuals into elite and non-elite individuals.

        The function will create two lists to separate out elite individuals i.e. ones with the highest fitness
        scores, from those with lower fitness scores. Top 10% of individuals (or at least 1) will be kept from
        a list. The rest will be assigned to a separate list, which will be updated using crossover and/or mutation.

        Returns:
            Tuple of List[Phenotype] and List[Phenotype] representing separate groups of
                elite and non_elite individuals.
        """
        sorted_individuals = self.sort_phenotypes_by_fitness_score(fitness_function)
        elite_individual_threshold = int(self.number_of_individuals * self.ratio_of_elite_individuals)
        elite_individuals = sorted_individuals[:elite_individual_threshold]
        non_elite_individuals = sorted_individuals[elite_individual_threshold:]
        shuffle(non_elite_individuals)
        return elite_individuals, non_elite_individuals

    def sort_phenotypes_by_fitness_score(self, fitness_function: AbstractFitnessFunction) -> List[AbstractPhenotype]:
        """Sort list of AbstractPhenotype by descending fitness score."""
        phenotype_and_fitness_score_tuple_list = []
        for phenotype in self.population:
            fitness_score = fitness_function.evaluate(phenotype)
            phenotype_and_fitness_score_tuple_list.append((phenotype, fitness_score))

        sorted_phenotype_tuples = sorted(phenotype_and_fitness_score_tuple_list,
                                         key=get_score_for_sorting, reverse=True)
        sorted_phenotypes = []
        for my_tuple in sorted_phenotype_tuples:
            sorted_phenotypes.append(my_tuple[0])

        return sorted_phenotypes


def get_score_for_sorting(phenotype_and_fitness_score_tuple: Tuple[AbstractPhenotype, int]) -> Union[float, int]:
    """Key for sorted function used in split_elite_individuals object.

    Provides a key for sorting individuals by returning the phenotype's fitness score from a tuple
    of phenotype and fitness score. This is used with python's sorted function.

    Args:
        phenotype_and_fitness_score_tuple: tuple of phenotype instance and its fitness score.
    Returns:
        Float or int equal to a phenotype's fitness score.
    """
    return phenotype_and_fitness_score_tuple[1]
