# Evolutionary-Optimization
A generic evolutionary algorithm for function optimization.

## Introduction
This package allows the user to optimise a function using an evolutionary algorithm.
An [evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm) 
uses the principles of evolution to find optimal solutions.

## Using the Package
### Getting Started 
To get started with this package install this package:

```bash
pip install evolutionary-optimization-algorithm
```

### Running Experiments
To run the code type the following in your terminal. The default experiment is a 
simple optimization of the $x^{2}$ using integers.
```bash
run_evolution
```
The parameters used for the run can be edited within the main.py file.

### Personalising Experiments
To personalise your experiment you can either use the prebuilt phenotypes and genotypes using our interface,
or you can build your own. 
To do so, you simply need to create a new phenotype / genotype class that 
inherits from the corresponding abstract class and implement the methods to suit your needs.
You can mimic the structure of the main script to run your own experiments, like so:
```python 
    genotype_class = Genotype.get_genotype(Genotypes.<your_phenotype>)
    phenotype_class = Phenotype.get_phenotype(Phenotypes.<your_genotype>)
    fitness_function_class = FitnessFunction.get_fitness_function(FitnessFunctions.<your_fitness_function>)
    fitness_function_instance = fitness_function_class()

    evolutionary_algorithm = Evolution(
        phenotype=phenotype_class(genotype_class()),
        number_of_individuals=<desired_number_of_individuals>,
        number_of_generations=<desired_number_of_generations>,
        fitness_function=fitness_function_instance,
        ratio_of_elite_individuals=<desired_elitism_ratio>
    )
```
You can also plot your fitness over time and the phenotype over time:
```python 
    evolutionary_algorithm.plot_fitness_score_over_time()
    phenotype_function_points_tuple = generate_points_for_function(
        phenotype=evolutionary_algorithm.population.best_individual,
        bottom_plotting_limit=-10,
        upper_plotting_limit=10,
        number_of_points=100,
    )
    evolutionary_algorithm.plot_phenotype_function_and_best_individuals(phenotype_function_points_tuple)
```
or plot a gif of the algorithm over time:
```python 
    evolutionary_algorithm.create_gif(phenotype_function_points_tuple)
```
