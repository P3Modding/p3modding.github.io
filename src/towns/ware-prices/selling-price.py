import logging
from matplotlib import pyplot as plt
import numpy as np
import math
import pytest

LOGGER = logging.getLogger()
# case1: f1=0.4
F_MAX = [math.nan, 1.4, 1.0, 0.7]
F_VAR = [1.4, 0.4, 0.3, 0.2]
F_DIFFICULTY = [2.2, 2.0, 1.8]
SAMPLE_THRESHOLDS = [20_000, 60_000, 70_000, 80_000]
PIG_IRON_BASE_PRICE = 0.44000003


def get_price(
    stock: int,
    sell_amount: int,
    thresholds: list[int],
    base_price: float,
    trade_difficulty: int,
) -> float:
    price = 0
    interval = 0
    new_stock = stock + sell_amount
    LOGGER.debug(f"get_price for {sell_amount} ({stock} -> {new_stock})")
    while interval < 4:
        if stock < thresholds[interval]:
            LOGGER.debug(f"Stock is smaller than t{interval}")
            # Stock is smaller than the lower bound of the interval, so we start selling
            interval_start = 0 if interval == 0 else thresholds[interval - 1]
            interval_end = thresholds[interval]
            interval_size = interval_end - interval_start
            w_interval_stock = max(stock, interval_start)
            w_relative_stock = (
                w_interval_stock - interval_start
            )  # Distance of stock from start of interval

            # Get the amount in the current bracket (i.e. everything until the next threshold or stock)
            w_s = min(sell_amount, interval_size - w_relative_stock)
            w_relative_new_stock = w_relative_stock + w_s

            f = get_factor(
                interval,
                w_relative_stock,
                w_relative_new_stock,
                interval_size,
                trade_difficulty,
            )
            bracket_price = base_price * w_s * f
            LOGGER.debug(f"Selling {w_s} in {interval} with f={f} for {bracket_price}")
            price += bracket_price
            sell_amount -= w_s

            if new_stock <= interval_end:
                break
        interval += 1

    if new_stock > thresholds[3]:
        interval_start = thresholds[3]
        w_s = new_stock - max(stock, interval_start)
        f = 0.5
        LOGGER.debug(f"Selling {w_s} above t3 with f={f}")
        price += base_price * w_s * f

    return price


def get_factor(
    interval: int,
    w_relative_stock: int,
    w_new_relative_stock: int,
    interval_width: int,
    trade_difficulty: int,
) -> int:
    LOGGER.debug(
        f"get_factor(interval={interval}, w_relative_stock={w_relative_stock}, w_new_relative_stock={w_new_relative_stock})"
    )
    if interval == 4:
        return 0.5
    else:
        middle = (w_relative_stock + w_new_relative_stock) / 2
        f_max = F_MAX[interval] if interval > 0 else F_DIFFICULTY[trade_difficulty]
        f_var = (
            F_VAR[interval]
            if interval > 0
            else (F_DIFFICULTY[trade_difficulty] - F_VAR[interval])
        )
        return f_max - f_var * (middle) / (interval_width)


def plot_example1():
    plt.clf()
    params = {"mathtext.default": "regular"}
    plt.rcParams.update(params)
    fig, (ax1) = plt.subplots(1, 1)
    x = []
    t0_f_y = []
    t0_pigiron_difficulty0_y = []
    t0_pigiron_difficulty1_y = []
    t0_pigiron_difficulty2_y = []
    for stock in range(2000, SAMPLE_THRESHOLDS[-1] + 10_000):
        # for stock in range(17000, 23000):
        x.append(stock)
        t0_pigiron_difficulty0_y.append(
            get_price(stock, 2000, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 0)
        )
        t0_pigiron_difficulty1_y.append(
            get_price(stock, 2000, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
        )
        t0_pigiron_difficulty2_y.append(
            get_price(stock, 2000, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 2)
        )
        if (
            len(t0_pigiron_difficulty0_y) > 2
            and t0_pigiron_difficulty0_y[-1] > t0_pigiron_difficulty0_y[-2]
        ):
            raise Exception(f"At {stock} stock, we have an increase in price")

    ax1.plot(x, t0_pigiron_difficulty0_y, label="low")
    ax1.plot(x, t0_pigiron_difficulty1_y, label="normal")
    ax1.plot(x, t0_pigiron_difficulty2_y, label="high")
    # """
    ax1.axvline(SAMPLE_THRESHOLDS[0])
    ax1.text(SAMPLE_THRESHOLDS[0], 0, "$t_0$", va="bottom")
    ax1.axvline(SAMPLE_THRESHOLDS[1])
    ax1.text(SAMPLE_THRESHOLDS[1], 0, "$t_1$", va="bottom")
    ax1.axvline(SAMPLE_THRESHOLDS[2])
    ax1.text(SAMPLE_THRESHOLDS[2], 0, "$t_2$", va="bottom")
    ax1.axvline(SAMPLE_THRESHOLDS[3])
    ax1.text(SAMPLE_THRESHOLDS[3], 0, "$t_3$", va="bottom")
    # """

    ax1.set_title("Selling Price of 1 Pigiron Bundle per Difficulty")
    ax1.set_xlabel("Stock")
    ax1.set_ylabel("Price")

    plt.legend()
    plt.tight_layout()
    plt.savefig("selling-price-pigiron.png", dpi=150)


def tests():
    stock = 0
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 0)
    assert price == pytest.approx(1900.80011844635)

    stock = 0
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(1733.600108027458)

    stock = 0
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 2)
    assert price == pytest.approx(1566.400097608566)

    stock = 0
    sell_amount = 50 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 0)
    assert price == pytest.approx(47740.00297486782)

    stock = 0
    sell_amount = 50 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(46860.00292003155)

    stock = 0
    sell_amount = 50 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 2)
    assert price == pytest.approx(45980.00286519527)

    stock = 17000
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(1284.800080060959)

    stock = 19000
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(1236.400077044964)

    stock = 21000
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(1214.400075674057)

    stock = 55000
    sell_amount = 50 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 2)
    assert price == pytest.approx(25135.00156626105)

    stock = 57000
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(897.6000559329987)

    stock = 77000
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(475.19997590064672)

    stock = 85000
    sell_amount = 1 * 2000
    price = get_price(stock, sell_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE, 1)
    assert price == pytest.approx(440)


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
tests()
plot_example1()
