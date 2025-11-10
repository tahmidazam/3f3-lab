import logging
from pathlib import Path

from matplotlib import pyplot as plt


def save_fig(question: int, name: str, directory: Path = Path("./../tex/plots")):
    path = directory / f"{str(question)}_{name}.pgf"

    fig = plt.gcf()
    axes = fig.get_axes()

    for ax in axes:
        ax.minorticks_on()
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

    plt.tight_layout()
    plt.savefig(path)

    logging.info(f"Saved figure to {path}")
