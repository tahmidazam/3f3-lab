import numpy as np


def calc_const_b(alpha: float, beta: float) -> float:
    return (1 / alpha) * np.arctan(beta * np.tan(np.pi * alpha / 2))
