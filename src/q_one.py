import logging

import numpy as np
from scipy.stats import norm, uniform

from plot_multinomial_theory import plot_multinomial_theory
from plot_pdf_and_estimate import plot_pdf_and_estimate


def q_one():
    logging.info("Q1: Uniform and random variables")

    plot_pdf_and_estimate(
        plot_id="normal",
        gen_fn=np.random.randn,
        pdf=lambda x: norm.pdf(x, 0, 1)
    )

    plot_pdf_and_estimate(
        plot_id="uniform",
        gen_fn=np.random.rand,
        pdf=lambda x: uniform.pdf(x, 0, 1),
        ks_density_width=0.15
    )

    plot_multinomial_theory(
        n_values=[100, 1_000, 10_000],
        subplot_titles=["A", "B", "C"],
    )
