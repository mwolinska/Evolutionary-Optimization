from evolutionary_optimization.evolutionary_algorithm.evolution import Evolution
from evolutionary_optimization.fitness_functions.fitness_interface import FitnessFunctions
from evolutionary_optimization.genotype.genotype_model.genotype_interface import Genotype, Genotypes
from evolutionary_optimization.phenotype.phenotype_model.phenotype_interface import Phenotype, Phenotypes
from evolutionary_optimization.phenotype.phenotype_model.phenotype_utils import generate_points_for_function


def run_evolutionary_alg():
    genotype_class = Genotype.get_genotype(Genotypes.FLOAT_LIST)
    phenotype_class = Phenotype.get_phenotype(Phenotypes.PARABOLA)

    evolutionary_algorithm = Evolution(
        phenotype=phenotype_class(
            genotype_class(
                ratio_of_population_for_crossover=0,
                mutation_probability=0,
            )
        ),
        number_of_individuals=10,
        number_of_generations=20,
        fitness_function=FitnessFunctions.MINIMIZE,
        ratio_of_elite_individuals=0.1,
    )
    evolutionary_algorithm.evolve()
    evolutionary_algorithm.plot_fitness_score_over_time()
    phenotype_function_points_tuple = generate_points_for_function(
        phenotype=evolutionary_algorithm.population.phenotype,
        bottom_plotting_limit=-10,
        upper_plotting_limit=10,
    )
    evolutionary_algorithm.plot_phenotype_function_and_best_individuals(phenotype_function_points_tuple)
    print()

if __name__ == '__main__':
   run_evolutionary_alg()
