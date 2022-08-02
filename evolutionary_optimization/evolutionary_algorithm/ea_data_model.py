from dataclasses import dataclass
from typing import Union


@dataclass
class PerformancePlotting:
    fitness_over_time: list[Union[float, int]]
    phenotype_over_time: list[Union[float, int]]
    genotype_over_time: list[Union[float, int]]
