from dataclasses import dataclass
from typing import Union, List


@dataclass
class PerformancePlotting:
    """Dataclass storing information about the algorithm's state overtime."""
    fitness_over_time: List[Union[float, int]]
    phenotype_over_time: List[Union[float, int]]
    genotype_over_time: List[Union[float, int, List[Union[float, int]]]]
