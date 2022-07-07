from typing import Tuple

from matplotlib import pyplot as plt

from fitness_functions import a_func
from individual import get_score_for_sorting
from population import Population


class Evolution:
    def __init__(self, n_individuals: int, n_generations: int, individual_value_range: Tuple[int, int]):
        self.population = Population(n_individuals, individual_value_range)
        self.epochs = n_generations
        self.fitness_over_time = []

    def evolve(self):
        for n in range(self.epochs):
            self.evaluate_population()
            self.update_population()
            self.record_performance()

        print(f"The value of the best individual is {self.population.best_individual.value}")
        self.plot_performance()

    def evaluate_population(self):

        for individual in self.population.all_individuals:
            fitness_score = a_func(individual.value)
            individual.fitness_score = fitness_score
            if self.population.best_individual.fitness_score is None or fitness_score > self.population.best_individual.fitness_score:
                self.population.best_individual = individual

    def update_population(self):
        sorted_individuals = sorted(self.population.all_individuals, key=get_score_for_sorting)
        self.population.all_individuals = sorted_individuals[:(self.population.n_individuals // 2)]
        n_individuals_to_replace = self.population.n_individuals - (self.population.n_individuals // 2)
        self.population.add_new_individuals(n_individuals_to_replace)

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
