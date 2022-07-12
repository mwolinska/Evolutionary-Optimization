from typing import Tuple

from matplotlib import pyplot as plt

from fitness_functions import a_func
from genotype import GenotypeKey, GenotypeProperties
from population import Population


class Evolution:
    def __init__(self,
                 n_individuals: int,
                 n_generations: int,
                 genotype_key: GenotypeKey = GenotypeKey.a_list,
                 n_genes: int = 1,
                 individual_value_range: Tuple[int, int] = (0, 1),
                 mutation_probability: float = 0.5,
                 crossover: bool = False
                 ):
        self.genotype_properties = GenotypeProperties(genotype_key, n_genes, individual_value_range, mutation_probability)
        self.population = Population(n_individuals, self.genotype_properties, crossover=crossover)
        self.epochs = n_generations
        self.fitness_over_time = []

    def evolve(self):
        for n in range(self.epochs):
            self.evaluate_population()
            self.population.update_population()
            self.record_performance()

        print(f"The value of the best individual is {self.population.best_individual.genotype.all_genes}")
        self.plot_performance()

    def evaluate_population(self):

        for individual in self.population.all_individuals:
            fitness_score = a_func(individual.genotype.all_genes)
            individual.fitness_score = fitness_score
            if self.population.best_individual.fitness_score is None or fitness_score > self.population.best_individual.fitness_score:
                self.population.best_individual = individual

    def record_performance(self):
        self.fitness_over_time.append(self.population.best_individual.fitness_score)

    def plot_performance(self):
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
