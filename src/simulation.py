import numpy as np
from matplotlib import pyplot as plt

from calc_const_b import calc_const_b
from calc_const_s import calc_const_s
from calc_rv_x import calc_rv_x
from constants import PAGE_WIDTH_IN_INCHES, PAGE_HEIGHT_IN_INCHES
from save_fig import save_fig


def simulation(
        alphas: list[float],
        betas: list[float],
        n: int = 100_000,
        k: int = 50,
) -> None:
    """
    Plots histogram density estimates for a set of alpha and beta values.

    :param alphas: The list of alpha values, where 0 <= alpha <= 2, alpha != 1.
    :param betas: The list of beta values, where beta -1 <= beta <= 1.
    :param n: The number of samples of X to plot.
    :param k: The number of histogram bins.
    """
    fig, axes = plt.subplots(
        nrows=len(betas),
        ncols=len(alphas),
        figsize=(PAGE_WIDTH_IN_INCHES, PAGE_HEIGHT_IN_INCHES * 0.8),
    )

    for i, beta in enumerate(betas):
        for j, alpha in enumerate(alphas):
            b = calc_const_b(alpha, beta)
            s = calc_const_s(alpha, beta)
            u = np.random.uniform(-np.pi / 2, np.pi / 2, size=n)
            v = np.random.exponential(scale=1, size=n)
            x = calc_rv_x(alpha, s, b, u, v)

            ax = axes[i, j]
            ax.tick_params(axis='both', which='major', labelsize="small")
            ax.hist(x, bins=k, label="histogram", color="black", density=True, log=True)

            if j == 0:
                ax.set_ylabel(rf"$\beta = {beta}$", fontsize="small")

            if i == 0:
                ax.set_title(rf"$\alpha = {alpha}$", fontsize="small", loc="left")

    save_fig(question=4, name="simulation")
