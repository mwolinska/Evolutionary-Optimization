from typing import Tuple

from matplotlib import pyplot as plt

from genotype.genotype_data_model import GenotypeProperties
from phenotype import a_func
from phenotype.phenotypes_interface import Phenotypes
from population import Population


class Evolution:
    def __init__(
        self,
        n_individuals: int,
        n_generations: int,
        genotype_key: type = list,
        type_of_gene: type = float,
        n_genes: int = 1,
        gene_value_range: Tuple[int, int] = (0, 1),
        mutation_probability: float = 0.5,
        phenotype: str = "test",
        crossover: bool = False
    ):
        """Initialises Evolution class.

        The evolution class performs evolutionary optimisation of a function (a phenotype).
        It contains a population of individuals that are evaluated at every iteration (generation)
        of the algorithm.

        Args:
            n_individuals: number of individuals in the desired population.
            n_generations: number of iterations of the algorithm.
            genotype_key: type of genotype using the GenotypeKey object.
            type_of_gene: type of gene within the genotype.
            n_genes: number of genes in an individual's genotype.
            gene_value_range: tuple of the minimum and maximum values of a gene.
            mutation_probability: probability of mutation of an individual when updating population.
            phenotype: phenotype used to understand the genotype.
            crossover: whether crossover should happen when updating the population.
        """

        self.genotype_properties = GenotypeProperties(genotype_key, type_of_gene, n_genes, gene_value_range, mutation_probability)
                                                      type_of_gene,
        self.population = Population(n_individuals,
                                     self.genotype_properties,
                                     phenotype=Phenotypes(phenotype),
                                     crossover=crossover)
        self.epochs = n_generations
        self.fitness_over_time = []

    def evolve(self):
        """Performs evolutionary optimisation.

        This function performs the evolutionary optimisation. Over n_generations it evaluates the population,
        updates the population (with crossover and/ or mutation as initialised). It then record the
        best fitness score at each generation. Once optimisation is complete it plots the performance over time.
        """
        for n in range(self.epochs):
            self.evaluate_population()
            self.population.update_population()
            self.record_performance()

        print(f"The value of the best individual is {self.population.best_individual.genotype.genotype}")
        self.plot_performance()

    def evaluate_population(self):
        """Calculates fitness scores for each individual in population.

        For each individual in the population calculates the fitness score and stores the best individual
        in the population.best_individual attribute.
        """
        for individual in self.population.all_individuals:
            fitness_score = a_func(individual.genotype.genotype)
            individual.fitness_score = fitness_score
            if self.population.best_individual.fitness_score is None or \
                    fitness_score > self.population.best_individual.fitness_score:
                self.population.best_individual = individual
        print(f"the best individual currently is at {self.population.best_individual.genotype.genotype}")
        print(f"the fitness score is {self.population.best_individual.fitness_score}")

    def record_performance(self):
        """Record fitness function value of the current best individual."""

        self.fitness_over_time.append(self.population.best_individual.fitness_score)
        print(f"the fitness over time is {self.fitness_over_time}")

    def plot_performance(self):
        """Plots score of the best individual at each generation."""
        x_axis = list(range(0, len(self.fitness_over_time)))
        plt.plot(x_axis, self.fitness_over_time)
        plt.title('Algorithm Performance Over Time')
        plt.xlabel('Epoch')
        plt.ylabel('Fitness score')
        plt.show()

if __name__ == '__main__':
    test_evolution = Evolution(n_individuals=10, n_generations=3, individual_value_range=(10, -10))
    test_evolution.evolve()
    print()
