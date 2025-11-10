import numpy as np
from matplotlib import pyplot as plt

from constants import PAGE_WIDTH_IN_INCHES
from save_fig import save_fig


def plot_multinomial_theory(
        n_values: list[int],
        subplot_titles: list[str],
        k: int = 30,
) -> None:
    """
    Plots histograms of the uniform distribution with overlaid horizontal
    lines for the theoretical mean and -3 and 3 times the standard deviation.

    :param n_values: The values for the sample count for each subplot.
    :param subplot_titles: The titles for each subplot.
    :param k: The number of histogram bins.
    """
    fig, axes = plt.subplots(figsize=(PAGE_WIDTH_IN_INCHES, 2), ncols=len(n_values), nrows=1)

    for i, (ax, n) in enumerate(zip(axes, n_values)):
        vector = np.random.rand(n)
        p = 1 / k
        theoretical_mean = n * p
        theoretical_std_dev = np.sqrt(n * p * (1 - p))
        counts, bin_edges, _ = ax.hist(vector, bins=k, color="lightgrey")

        ax.hlines(
            theoretical_mean, bin_edges[0], bin_edges[-1],
            color="black",
            label="$E[X_j]$",
        )

        three_std_dev_lines = [
            theoretical_mean + 3 * theoretical_std_dev,
            theoretical_mean - 3 * theoretical_std_dev
        ]
        ax.hlines(
            three_std_dev_lines,
            bin_edges[0], bin_edges[-1],
            color="black",
            linestyle="dashed",
            label=r"$E[X_j] \pm 3\sigma$"
        )

        ax.set_xlabel("value")
        ax.set_title(subplot_titles[i], fontsize="small", loc="left", fontweight="bold")

    axes[0].set_ylabel("count")
    axes[-1].legend(fontsize="x-small", loc="lower right")

    save_fig(question=1, name="uniform_multinomial")
