import logging

import matplotlib


def init_matplotlib() -> None:
    matplotlib.use("pgf")

    matplotlib.rcParams.update({
        "pgf.preamble": r"\usepackage{amsmath}",
        "pgf.texsystem": "pdflatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })

    logging.info("matplotlib initialised")
