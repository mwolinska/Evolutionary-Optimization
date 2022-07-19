from phenotype.abstract_phenotype import AbstractPhenotype


class MSE(AbstractPhenotype):

    def function_to_optimise(self):
        print("woo x 2")
        pass

    @property
    def fitness_function(self):
        pass

    # @fitness_function.setter
    # pa
