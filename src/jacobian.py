import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

from constants import PAGE_WIDTH_IN_INCHES
from save_fig import save_fig


def jacobian(
        a: float = 10,
        b: float = 10,
        n: int = 10_000,
        bin_count: int = 30,
        linspace_num: int = 1_000,
):
    """
    Plots histograms of linear [f(x) = ax + b] and square [f(x) = x^2] transformations of
    samples from the normal distribution, overlaid with the theoretical pdfs calculated
    using the Jacobian.

    :param a: The value of constant a.
    :param b: The value of constant b.
    :param n: The number of samples taken from the normal distribution.
    :param bin_count: The number of histogram bins.
    :param linspace_num: The number of points to evaluate the pdfs at.
    """
    x = np.random.randn(n)
    y_linear = a * x + b
    y_square = x ** 2
    y_linear_vals = np.linspace(min(y_linear), max(y_linear), num=linspace_num)
    y_square_vals = np.linspace(
        start=1e-6,  # Avoid division by 0
        stop=max(y_square),
        num=linspace_num
    )
    p_y_linear = (1 / abs(a)) * norm.pdf((y_linear_vals - b) / a)
    p_y_square = np.array([
        0.5 / np.sqrt(val) * (norm.pdf(np.sqrt(val)) + norm.pdf(-np.sqrt(val)))
        for val in y_square_vals
    ])

    fig, (linear_ax, square_ax) = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(PAGE_WIDTH_IN_INCHES, 2)
    )

    linear_ax.hist(y_linear, bins=bin_count, color="lightgrey", density=True)
    linear_ax.plot(y_linear_vals, p_y_linear, color="black")
    counts_square, _, _ = square_ax.hist(y_square, bins=bin_count, color="lightgrey", density=True)
    square_ax.plot(y_square_vals, p_y_square, color="black")

    max_bin_count = counts_square.max()
    square_ax.set_ylim(top=1.2 * max_bin_count)  # Limit y-axis due to large values close to 0.
    linear_ax.set_xlabel("value")
    square_ax.set_xlabel("value")
    linear_ax.set_ylabel("probability density")
    linear_ax.set_title("A", fontsize="small", loc="left", fontweight="bold")
    square_ax.set_title("B", fontsize="small", loc="left", fontweight="bold")

    save_fig(question=2, name="jacobian")
