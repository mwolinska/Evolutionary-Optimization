from typing import Tuple, Union, List

from matplotlib import pyplot as plt
from tqdm import tqdm

from evolutionary_optimization.evolutionary_algorithm.ea_data_model import PerformancePlotting
from evolutionary_optimization.evolutionary_algorithm.population import Population
from evolutionary_optimization.fitness_functions.fitness_interface import FitnessFunctions, FitnessFunction
from evolutionary_optimization.phenotype.phenotype_model.abstract_phenotype import AbstractPhenotype


class Evolution:
    def __init__(
        self,
        phenotype: AbstractPhenotype,
        fitness_function: FitnessFunctions = FitnessFunctions.MAXIMIZE,
        number_of_individuals: int = 100,
        number_of_generations: int = 20,
        ratio_of_elite_individuals: float = 0.1,
    ):
        """Initialise Evolution class.

        The Evolution class performs evolutionary optimization of a function (a phenotype).
        It contains a population of individuals that are evaluated at every iteration (generation)
        of the algorithm.

        Args:
            phenotype: a phenotype instance with the desired genotype.
            fitness_function: desired fitness function from interface.
            number_of_individuals: number of phenotype instances to be used within the population.
            number_of_generations: number of times the algorithm will be run.
            ratio_of_elite_individuals: proportion of best scoring phenotypes in population that will be kept
                to the next generation.
        """
        self.population = Population(number_of_individuals, phenotype, ratio_of_elite_individuals)
        self.epochs = number_of_generations
        self.fitness_function = FitnessFunction.get_fitness_function(fitness_function)
        self.performance_over_time = PerformancePlotting(
            fitness_over_time=[],
            phenotype_over_time=[],
            genotype_over_time=[],
        )

    def evolve(self):
        """Perform evolutionary optimisation.

        This function performs the evolutionary optimisation. Over number_of_generations it evaluates the population,
        updates the population (with crossover and/ or mutation as initialised). It then records the
        best fitness score at each generation.
        """
        for epoch in tqdm(range(self.epochs)):
            self.population.evaluate_population(self.fitness_function())
            self.population.update_population(self.fitness_function())
            self.record_performance()

        print(f"The value of the best individual is {self.population.best_individual.genotype.genotype}")

    def record_performance(self):
        """In place addition of fitness score, phenotype and genotype values of the current best individual.

        This function performs in place addition of the current best fitness score, phenotype value
        and genotype value to the performance_over_time attribute.
        You can visualise fitness over time using the plot_fitness_score_over_time function, and you can visualise
        phenotype and genotype values over time using plot_phenotype_function_and_best_individuals function.
        """
        self.performance_over_time.fitness_over_time.append(self.fitness_function().evaluate(
            phenotype=self.population.best_individual)
        )
        self.performance_over_time.phenotype_over_time.append(self.population.best_individual.phenotype_value)
        self.performance_over_time.genotype_over_time.append(self.population.best_individual.genotype.genotype[0])
        print(self.population.best_individual.phenotype_value)

    def plot_fitness_score_over_time(self):
        """Plot score of the best individual at each generation."""
        x_axis = list(range(0, len(self.performance_over_time.fitness_over_time)))
        plt.plot(x_axis, self.performance_over_time.fitness_over_time)
        plt.title('Algorithm Performance Over Time')
        plt.xlabel('Epoch')
        plt.ylabel('Fitness score')
        plt.show()

    def plot_phenotype_function_and_best_individuals(
            self,
            function_tuple: Tuple[List[Union[int, float]], List[Union[int, float]]],
    ):
        """Plot phenotype function and best individual phenotype values."""
        plt.plot(function_tuple[0], function_tuple[1], label="Phenotype Function")
        plt.plot(
            self.performance_over_time.genotype_over_time,
            self.performance_over_time.phenotype_over_time,
            label="Best Individual Over Time"
        )
        plt.title('Phenotype Function and Best Predictions')
        plt.xlabel('Genotype')
        plt.ylabel('Phenotype')
        plt.legend()
        plt.show()
