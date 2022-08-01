from evolutionary_optimization.evolutionary_algorithm.evolution import Evolution
from evolutionary_optimization.fitness_functions.fitness_interface import FitnessFunctions
from evolutionary_optimization.genotype.genotype_interface import Genotype, Genotypes
from evolutionary_optimization.phenotype.phenotype_interface import Phenotype, Phenotypes


def run_evolutionary_alg():
    genotype_class = Genotype.get_genotype(Genotypes.BINARY_LIST)
    phenotype_class = Phenotype.get_phenotype(Phenotypes.PARABOLA)

    evolutionary_algorithm = Evolution(
        phenotype=phenotype_class(genotype_class()),
        number_of_individuals=100,
        number_of_generations=10,
        fitness_function=FitnessFunctions.MINIMIZE,
        ratio_of_elite_individuals=0.1
    )
    evolutionary_algorithm.evolve()
    evolutionary_algorithm.plot_performance()

if __name__ == '__main__':
   run_evolutionary_alg()
