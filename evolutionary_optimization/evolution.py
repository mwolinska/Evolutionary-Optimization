from matplotlib import pyplot as plt

from evolutionary_optimization.population import Population
from fitness_score.fitness_interface import FitnessFunctions, FitnessFunction
from genotype.integer_list_genotype import IntegerListGenotype
from phenotype.abstract_phenotype import AbstractPhenotype
from phenotype.parabola_phenotype import ParabolaPhenotype


class Evolution:
    def __init__(
        self,
        phenotype: AbstractPhenotype,
        fitness_function: FitnessFunctions,
        number_of_individuals: int,
        number_of_generations: int,
    ):
        """Initialises Evolution class.

        The evolutionary_optimization class performs evolutionary optimisation of a function (a phenotype_folder).
        It contains a population of individuals that are evaluated at every iteration (generation)
        of the algorithm.

        Args:
        """
        self.population = Population(number_of_individuals, phenotype)
        self.epochs = number_of_generations
        self.fitness_over_time = []
        self.fitness_function = FitnessFunction().get_fitness_function(fitness_function)

    def evolve(self):
        """Performs evolutionary optimisation.

        This function performs the evolutionary optimisation. Over n_generations it evaluates the population,
        updates the population (with crossover and/ or mutation as initialised). It then record the
        best fitness score at each generation. Once optimisation is complete it plots the performance over time.
        """
        for n in range(self.epochs):
            self.population.evaluate_population(self.fitness_function())
            self.population.update_population(self.fitness_function())
            self.record_performance()

        print(f"The value of the best individual is {self.population.best_individual.genotype.genotype}")
        self.plot_performance()

    # def evaluate_population(self):
    #     """Calculates fitness scores for each individual in population.
    #
    #     For each individual in the population calculates the fitness score and stores the best individual
    #     in the population.best_individual attribute.
    #     """
    #     for individual in self.population.population:
    #         fitness_score = individual.calculate_fitness_score()
    #
    #         individual.fitness_functions_dictionary = fitness_score
    #         if self.population.best_individual.fitness_functions_dictionary is None or \
    #                 fitness_score > self.population.best_individual.fitness_functions_dictionary:
    #             self.population.best_individual = individual

    def record_performance(self):
        """Record fitness function value of the current best individual."""

        self.fitness_over_time.append(self.fitness_function().evaluate(phenotype=self.population.best_individual))

    def plot_performance(self):
        """Plots score of the best individual at each generation."""
        x_axis = list(range(0, len(self.fitness_over_time)))
        plt.plot(x_axis, self.fitness_over_time)
        plt.title('Algorithm Performance Over Time')
        plt.xlabel('Epoch')
        plt.ylabel('Fitness score')
        plt.show()
