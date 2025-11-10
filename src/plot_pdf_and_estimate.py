from typing import Callable

import numpy as np
from matplotlib import pyplot as plt

from constants import PAGE_WIDTH_IN_INCHES
from ksdensity import ksdensity
from save_fig import save_fig


def plot_pdf_and_estimate(
        plot_id: str,
        gen_fn: Callable[[int], np.ndarray],
        pdf: Callable[[np.ndarray], np.ndarray],
        ks_density_width: float = 0.3,
        n: int = 1_000,
        bin_count: int = 30,
        linspace_num: int = 1_000,
):
    """
    Plots the histogram estimate and KDE of a given distribution.

    :param plot_id: The id of the plot used to name the exported file.
    :param gen_fn: The function used to generate samples.
    :param pdf: The probability density function.
    :param ks_density_width: The width used for the KDE.
    :param n: The number of samples.
    :param bin_count: The number of histogram bins.
    :param linspace_num: The number of points to evaluate the KDE at.
    """
    samples = gen_fn(n)
    samples_min = np.min(samples)
    samples_max = np.max(samples)
    x = np.linspace(samples_min, samples_max, linspace_num)
    pdf_values = pdf(x)
    ks_density = ksdensity(samples, width=ks_density_width)

    fig, (hist_ax, ksd_ax) = plt.subplots(
        figsize=(PAGE_WIDTH_IN_INCHES, 2),
        ncols=2,
        nrows=1,
        sharey=True
    )
    counts, bin_edges, _ = hist_ax.hist(
        samples,
        bins=bin_count,
        color="lightgrey",
        label="estimate"
    )

    bin_width = bin_edges[1] - bin_edges[0]
    scaled_pdf = pdf_values * bin_width * n
    scaled_ksd = ks_density(x) * bin_width * n

    hist_ax.plot(x, scaled_pdf, label="pdf", color="black")
    ksd_ax.plot(x, scaled_pdf, label="pdf", color="black")
    ksd_ax.plot(x, scaled_ksd, label="estimate", color="black", linestyle="dashed")

    ylim = np.max(counts) * 1.1

    for ax in [hist_ax, ksd_ax]:
        ax.set_ylim(bottom=0, top=ylim)
        ax.set_xlim(left=samples_min, right=samples_max)
        ax.set_xlabel("value")
        ax.set_ylabel("count")
        ax.legend(fontsize="x-small", loc="lower center")

    hist_ax.set_title("A", fontsize="small", loc="left", fontweight="bold")
    ksd_ax.set_title("B", fontsize="small", loc="left", fontweight="bold")

    save_fig(question=1, name=plot_id)
