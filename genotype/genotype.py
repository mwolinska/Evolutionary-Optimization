import random
from typing import List

import numpy as np

from genotype.genotype_data_model import GenotypeKey, Gene, GenotypeProperties

class Genotype:
    def __init__(self, genotype_properties: GenotypeProperties):
        """Object containing genotype information for an Individual.

        Args:
            genotype_properties: all properties required to build a genotype.

        """
        self.genotype = self.build_genotype(genotype_properties)
        self.genotype_key = genotype_properties.genotype_key
        self.value_range = genotype_properties.value_range
        self.mutation_probability = genotype_properties.mutation_probability
        self.gene_type = self.find_type_of_gene()

    def mutate(self):
        """Calls the correct method to perform a mutation based on GenotypeKey."""
        if self.genotype_key == GenotypeKey.STRING:
            new_genotype = self.mutate_string()
        elif self.genotype_key == GenotypeKey.LIST:
            new_genotype = self.mutate_list()
        else:
            raise NotImplementedError

        return new_genotype

    def mutate_string(self) -> str:
        """Performs mutation of a string object."""
        # TODO method not correctly implemented
        new_genotype = ""

        for gene in self.genotype:
            mutation = np.random.choice([True, False], p=[self.mutation_probability, 1 - self.mutation_probability])

            if mutation:
                my_list = [1, 0]
                new_gene = my_list[gene]
            else:
                new_gene = gene

            new_genotype += new_gene

        return new_genotype

    def mutate_list(self) -> List:
        """Performs mutation on a list.

        Based on the mutation probability each gene is either replaced by a random gene of the same type
        or kept.

        Returns:
            List
        """
        new_genotype = []

        for gene in self.genotype:
            mutation = np.random.choice([True, False], p=[self.mutation_probability, 1 - self.mutation_probability])

            # here vary depending on type of gene
            if mutation:
                # my_list = [1, 0]
                # new_gene = my_list[gene]
                new_gene = random.randint(self.value_range[0], self.value_range[1])

            else:
                new_gene = gene

            new_genotype.append(new_gene)

        return new_genotype

    @staticmethod
    def build_genotype(genotype_properties: GenotypeProperties):
        """Builds genotype based on requirements defined by genotype_properties.

        Args:
            genotype_properties: all genotype properties required to build genotype.
        Returns:
            Type aligned to the one defined by GenotypeKey. Currently, list or str
        """
        all_genes = None
        if genotype_properties.genotype_key == "list":
            all_genes = []
            for i in range(genotype_properties.n_genes):
                new_gene = random.randint(genotype_properties.value_range[0], genotype_properties.value_range[1])
                all_genes.append(new_gene)

        return all_genes

    def find_type_of_gene(self) -> Gene:
        """Finds type of gene within genotype.

        Checks whether genotype is binary (for both GenotypeKey == LIST and GenotypeKey == STRING),
        then checks type of first element in genotype.

        Returns:
            Gene.
        """
        if self.check_if_binary():
            return Gene.BINARY
        elif isinstance(self.genotype[0], int):
            return Gene.INTEGER
        elif isinstance(self.genotype[0], str):
            return Gene.STRING
        elif isinstance(self.genotype[0], float):
            return Gene.FLOAT
        else:
            raise NotImplementedError

    def check_if_binary(self):
        for el in self.genotype:
            if int(el) != 1 and int(el) != 0:
                return False
        return True


if __name__ == '__main__':

    print()
