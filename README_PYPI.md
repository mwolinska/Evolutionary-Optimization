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
pip install evolutionary_optimization
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
