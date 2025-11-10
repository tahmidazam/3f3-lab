import logging

from init_matplotlib import init_matplotlib
from q_four import q_four
from q_one import q_one
from q_three import q_three
from q_two import q_two


def main():
    logging.basicConfig(level=logging.INFO)

    init_matplotlib()

    q_one()
    q_two()
    q_three()
    q_four()


if __name__ == '__main__':
    main()
