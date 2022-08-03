from typing import List



def single_point_crossover(
        parent_1_genotype: List[int],
        parent_2_genotype: List[int],
        gene_slice_index: int,
) -> List[int]:
    """A single point crossover for genotype of type list.

    This is a single point crossover. Using the gene_slice_index, for both parents the genotype are sliced.
    The slice [:gene_slice_index] is taken from parent_1 and the slice [gene_slice_index:] is taken from parent_2.
    The two complementary slices are then joined to create a new genotype (a child genotype).

    Args:
        parent_1_genotype: genotype which will be used to create an offspring.
        parent_2_genotype: genotype which will be used to create an offspring.
        gene_slice_index: random integer at which the parent genotypes will be sliced.

    Returns:
        A genotype used to build a Genotype object.
    """
    child_genotype_part_1 = parent_1_genotype[:gene_slice_index]
    child_genotype_part_2 = parent_2_genotype[gene_slice_index:]
    child_genotype = child_genotype_part_1 + child_genotype_part_2
    return child_genotype
