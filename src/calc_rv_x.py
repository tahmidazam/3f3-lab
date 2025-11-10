import numpy as np


def calc_rv_x(
        alpha: float,
        s: float,
        b: float,
        u: np.ndarray,
        v: np.ndarray
) -> np.ndarray:
    return s * ((np.sin(alpha * (u + b))) / (np.power(
        np.cos(u),
        1 / alpha
    ))) * np.power(
        ((np.cos(u - alpha * (u + b))) / (v)),
        (1 - alpha) / alpha
    )
