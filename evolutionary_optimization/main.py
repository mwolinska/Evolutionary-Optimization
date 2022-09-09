from evolutionary_optimization.evolutionary_algorithm.evolution import Evolution
from evolutionary_optimization.fitness_functions.fitness_interface import FitnessFunctions, FitnessFunction
from evolutionary_optimization.genotype.genotype_model.genotype_interface import Genotype, Genotypes
from evolutionary_optimization.phenotype.implemented_phenotypes.booth_phenotype import BoothPhenotype
from evolutionary_optimization.phenotype.phenotype_model.phenotype_interface import Phenotype, Phenotypes
from evolutionary_optimization.phenotype.phenotype_model.phenotype_utils import generate_points_for_function


def run_evolutionary_alg():
    genotype_class = Genotype.get_genotype(Genotypes.INTEGER_LIST)
    phenotype_class = Phenotype.get_phenotype(Phenotypes.BOOTH)
    fitness_function_class = FitnessFunction.get_fitness_function(FitnessFunctions.MINIMIZE)
    fitness_function_instance = fitness_function_class()

    evolutionary_algorithm = Evolution(
        phenotype=phenotype_class(
            genotype_class(
                number_of_genes=2,
                mutation_probability=0.5,
            )
        ),
        number_of_individuals=100,
        number_of_generations=100,
        fitness_function=fitness_function_instance,
        ratio_of_elite_individuals=0.3,
    )
    evolutionary_algorithm.evolve()
    evolutionary_algorithm.plot_fitness_score_over_time()
    phenotype_function_points_tuple = generate_points_for_function(
        phenotype=evolutionary_algorithm.population.best_individual,
        bottom_plotting_limit=-10,
        upper_plotting_limit=10,
        number_of_points=100,
    )
    evolutionary_algorithm.plot_phenotype_function_and_best_individuals(phenotype_function_points_tuple)
    evolutionary_algorithm.create_gif(phenotype_function_points_tuple)

if __name__ == '__main__':
   run_evolutionary_alg()
