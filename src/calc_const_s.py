import numpy as np


def calc_const_s(alpha: float, beta: float) -> float:
    return np.power(
        1 + np.power(beta, 2) * np.power(np.tan(np.pi * alpha / 2), 2),
        1 / (2 * alpha)
    )
