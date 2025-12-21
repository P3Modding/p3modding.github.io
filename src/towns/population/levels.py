import logging
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import math
import pytest

LOGGER = logging.getLogger()
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


class Town:
    citizens: list[int]
    satisfactions: list[int]
    has_mint: bool
    dwellings_capacity: list[int]

    def __init__(
        self,
        rich: int,
        wealthy: int,
        poor: int,
        satifsaction_rich: int,
        satisfaction_wealthy: int,
        satisfaction_poor: int,
        has_mint: bool = False,
        dwellings_capacity_rich: int = 999999,
        dwellings_capacity_wealthy: int = 999999,
        dwellings_capacity_poor: int = 999999,
    ):
        self.citizens = [rich, wealthy, poor]
        self.satisfactions = [
            satifsaction_rich,
            satisfaction_wealthy,
            satisfaction_poor,
        ]
        self.has_mint = has_mint
        self.dwellings_capacity = [
            dwellings_capacity_rich,
            dwellings_capacity_wealthy,
            dwellings_capacity_poor,
        ]

    def update_population_levels(self):
        self.update_population_level(0)
        self.update_population_level(1)
        # TODO poor emigration

    def update_population_level(self, level: int):
        target = (
            self.citizens[2]
            * (self.satisfactions[level] + 40)
            // self.get_divisor(level)
        )
        target = min(max(target, 1), self.dwellings_capacity[level])
        LOGGER.debug(f"{level} target: {target} stock: {self.citizens[level]}")
        if target < self.citizens[level]:
            # Current stock exceeds target
            demoted = 2 * self.citizens[level] // target + 1
            if demoted > self.citizens[level]:
                demoted = self.citizens[level] - 1
            self.citizens[2] += demoted
            self.citizens[level] -= demoted
        else:
            # Target exceeds current stock
            if self.citizens[level]:
                promoted = 2 * target // self.citizens[level] + 1
            else:
                promoted = 1  # Avoid division by zero
            if self.citizens[2] > promoted:
                LOGGER.debug(f"promoting {promoted} poors to {level}")
                self.citizens[2] -= promoted
                self.citizens[level] += promoted

    def get_divisor(self, level):
        if level == 0:
            return 213 if self.has_mint else 320
        elif level == 1:
            return 160
        raise Exception()


def plot_example1():
    plt.clf()
    labels = ["Rich", "Wealthy", "Poor"]
    fig, (axs) = plt.subplots(1, 4, sharey="all", sharex="all", figsize=(10, 4))
    plot_example1_subplot(axs[0], 5, False, True)
    plot_example1_subplot(axs[1], 5, True)
    plot_example1_subplot(axs[2], 80, False)
    plot_example1_subplot(axs[3], 80, True)

    ax2 = axs[-1].twinx()
    ax2.set_ylim(*axs[-1].get_ylim())
    ax2.yaxis.set_major_formatter(PercentFormatter(1000))

    fig.suptitle("Convergence of 1000 Inhabitants")
    fig.legend(
        labels,
        bbox_to_anchor=(1, 1),
        loc="upper left",
        # bbox_transform=plt.gcf().transFigure,
    )
    plt.tight_layout()
    plt.savefig("levels1.png", dpi=100, bbox_inches="tight")


def plot_example1_subplot(ax, satisfaction: int, has_mint: bool, label: bool = False):
    ax.grid(axis="y")
    town = Town(50, 50, 900, satisfaction, satisfaction, satisfaction, has_mint)
    x = []
    sat_y_rich = []
    sat_y_wealthy = []
    sat_y_poor = []
    for i in range(0, 10):
        town.update_population_levels()
    for i in range(0, 60):
        x.append(i)
        sat_y_poor.append(town.citizens[2])
        sat_y_wealthy.append(town.citizens[1])
        sat_y_rich.append(town.citizens[0])
        town.update_population_levels()

    ax.plot(x, sat_y_rich, label="Rich")
    ax.plot(x, sat_y_wealthy, label="Wealthy")
    ax.plot(x, sat_y_poor, label="Poor")
    ax.set_xlabel("Days")
    if label:
        ax.set_ylabel("Inhabitants (absolute)")
    ax.set_title(f"{satisfaction} Satisfaction {"(Mint)" if has_mint else "(no Mint)"}")


plot_example1()
