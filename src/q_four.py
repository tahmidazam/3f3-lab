import logging

from simulation import simulation


def q_four():
    logging.info("Q4: Simulation from a 'difficult' density")

    simulation(alphas=[0.5, 1.5], betas=[-1, -0.5, 0, 0.5, 1])
