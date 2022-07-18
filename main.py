from evolution import Evolution
from genotype import GenotypeKey


def run_evolution():
    test_evolution = Evolution(n_individuals=5,
                               n_generations=4,
                               genotype_key=GenotypeKey.LIST,
                               n_genes=1,
                               gene_value_range=(-10, 10),
                               mutation_probability=1,
                               crossover=True)
    test_evolution.evolve()

if __name__ == '__main__':
    run_evolution()
