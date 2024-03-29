[![CircleCI](https://dl.circleci.com/status-badge/img/gh/mwolinska/Evolutionary-Optimization/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/mwolinska/Evolutionary-Optimization/tree/main)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/mwolinska/Evolutionary-Optimization/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/mwolinska/Evolutionary-Optimization/tree/main)

# Evolutionary-Optimization
A generic evolutionary algorithm for function optimization.

## Introduction
This package allows the user to optimise a function using an evolutionary algorithm.
An [evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm) uses the principles of evolution to find optimal solutions.
At a high level diagram of the process is as follows:

```mermaid
flowchart TD;

    A[Generate population] --> B[Evaluate population];
    B --> C{Is exit condition met?};
    C --No--> D[Update population];
    C --Yes--> E[Exit algorithm];
    D --> B
```

Currently, the only exit condition for the code is running the desired
number of generations.

## Using the Package
### Getting Started 
To get started with this package clone this repo:

```bash
git clone https://github.com/mwolinska/Evolutionary-Optimization
```
Then enter the correct directory on your machine:
```bash
cd Evolutionary-Optimization
```
This package uses [poetry](https://python-poetry.org) dependency manager. 
To install all dependencies run:

```bash
poetry install
```

Alternatively you can install the pypi package using pip:
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

```python
    genotype_class = Genotype.get_genotype(Genotypes.FLOAT_LIST)
    phenotype_class = Phenotype.get_phenotype(Phenotypes.PARABOLA)
    fitness_function_class = FitnessFunction.get_fitness_function(FitnessFunctions.MINIMIZE)
    fitness_function_instance = fitness_function_class()

    evolutionary_algorithm = Evolution(
        phenotype=phenotype_class(genotype_class()),
        number_of_individuals=10,
        number_of_generations=5,
        fitness_function=fitness_function_instance,
        ratio_of_elite_individuals=0.1
    )
```

This will produce the following output:
```bash
The value of the best individual is [-0.2240206935262563]
```

To generate the graph of fitness over time use:
```python
    evolutionary_algorithm.plot_performance()
```
within the run_evolution function to produce the following output:

<p align="center">
<img height="400" src="./Images/algorithm_plots/sample_evolution_over_time.png">
</p>

To generate the graph of the phenotype function and best individual phenotype / genotype 
pairs, use:
```python
    # generate points to plot the phenotype function
    phenotype_function_points_tuple = generate_points_for_function(
        phenotype=evolutionary_algorithm.population.phenotype,
        bottom_plotting_limit=-10,
        c=10,
    )
    # plot phenotype function and best individual phenotype / genotype pairs
    evolutionary_algorithm.plot_phenotype_function_and_best_individuals(phenotype_function__points_tuple)
```

To produce the following output:

<p align="center">
    <img height="400" src="./Images/algorithm_plots/phenotype_func_and_best_individuals.png"/>
</p>

### Personalising Experiments
To personalise your experiment you can either use the prebuilt phenotypes and genotypes using our interface,
or you can build your own. 
To do so, you simply need to create a new phenotype / genotype class that 
inherits from the corresponding abstract class and implement the methods to suit your needs.

The classes structure is outlined in the diagram below
<img  src="./Images/code_structure/classes_structure_diagram.svg"/>

The implemented fitness functions are outlined in the diagram below.
<img src="./Images/code_structure/abstract_fitness_functions_diagram.svg"/>

### Documentation
You can consult our documentation [here](https://mwolinska.github.io/Evolutionary-Optimization/).
