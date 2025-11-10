import numpy as np
from matplotlib import pyplot as plt

from constants import PAGE_WIDTH_IN_INCHES
from ksdensity import ksdensity
from save_fig import save_fig


def inverse_cdf(
        ks_density_width: float = 0.15,
        n: int = 10_000,
        k: int = 30,
        linspace_num: int = 1_000,
):
    """
    Plots the histogram estimate and the KDE for the exponential
    distribution with mean 1 using the inverse cdf method.

    :param ks_density_width: The width used in the KDE.
    :param n: The number of samples from the uniform distribution.
    :param k: The number of histogram bins.
    :param linspace_num: The number of points to evaluate the KDE at.
    """
    u_samples = np.random.rand(n)
    exp_samples = -np.log(1 - u_samples)
    x = np.linspace(
        start=exp_samples.min(),
        stop=exp_samples.max(),
        num=linspace_num
    )
    pdf = np.exp(-x)
    ks_density = ksdensity(exp_samples, width=ks_density_width)

    fig, (hist_ax, ksd_ax) = plt.subplots(figsize=(PAGE_WIDTH_IN_INCHES, 2), nrows=1, ncols=2)

    hist_ax.plot(x, pdf, color="black", linestyle="dashed", label="pdf")
    ksd_ax.plot(x, pdf, color="black", linestyle="dashed", label="pdf")
    hist_ax.hist(exp_samples, bins=k, color="lightgrey", density=True, label="estimate")
    ksd_ax.plot(x, ks_density(x), color="black", label="pdf")

    hist_ax.set_ylabel("probability density")
    hist_ax.set_title("A", fontsize="small", loc="left", fontweight="bold")
    ksd_ax.set_title("B", fontsize="small", loc="left", fontweight="bold")

    for ax in [hist_ax, ksd_ax]:
        ax.legend(fontsize="x-small")
        ax.set_xlabel("value")

    save_fig(question=3, name="inverse_cdf")
