from matplotlib import pyplot as plt
from tqdm import tqdm

from evolutionary_optimization.population import Population
from evolutionary_optimization.fitness_functions.fitness_interface import FitnessFunctions, FitnessFunction
from evolutionary_optimization.phenotype.abstract_phenotype import AbstractPhenotype


class Evolution:
    def __init__(
        self,
        phenotype: AbstractPhenotype,
        fitness_function: FitnessFunctions = FitnessFunctions.MAXIMIZE,
        number_of_individuals: int = 100,
        number_of_generations: int = 20,
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
        """
        self.population = Population(number_of_individuals, phenotype)
        self.epochs = number_of_generations
        self.fitness_over_time = []
        self.fitness_function = FitnessFunction().get_fitness_function(fitness_function)

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
        self.plot_performance()

    def record_performance(self):
        """In place addition of fitness function value of the current best individual.

        This function performs in place addition of the current best fitness score to the
        fitness_over_time attribute. Visualise using the plot_performance function.
        """
        self.fitness_over_time.append(self.fitness_function().evaluate(phenotype=self.population.best_individual))

    def plot_performance(self):
        """Plot score of the best individual at each generation."""
        x_axis = list(range(0, len(self.fitness_over_time)))
        plt.plot(x_axis, self.fitness_over_time)
        plt.title('Algorithm Performance Over Time')
        plt.xlabel('Epoch')
        plt.ylabel('Fitness score')
        plt.show()
