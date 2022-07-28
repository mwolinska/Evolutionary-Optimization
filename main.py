from evolutionary_optimization.evolution import Evolution
from fitness_functions.fitness_interface import FitnessFunctions
from genotype.genotype_interface import Genotype, Genotypes
from phenotype.phenotype_interface import Phenotype, Phenotypes

if __name__ == '__main__':
    genotype_class = Genotype().get_genotype(Genotypes.BINARY_LIST)
    phenotype_class = Phenotype().get_phenotype(Phenotypes.PARABOLA)

    evolutionary_algorithm = Evolution(phenotype=phenotype_class(genotype_class()),
                                       number_of_individuals=100,
                                       number_of_generations=10,
                                       fitness_function=FitnessFunctions.MINIMIZE
                                       )
    evolutionary_algorithm.evolve()
