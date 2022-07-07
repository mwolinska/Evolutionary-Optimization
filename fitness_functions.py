from typing import List


def MSE(predicted_value: float, expected_value: float):
    return (expected_value - predicted_value) ** 2

def a_func(x):
    y = x ** 2 * -1
    # y = -1 * x * (x - 1) * (x - 2) * (x - 3) * (x - 4)
    return y
