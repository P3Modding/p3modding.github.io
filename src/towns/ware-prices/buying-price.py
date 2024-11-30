import logging
from matplotlib import pyplot as plt
import numpy as np
import math
import pytest

LOGGER = logging.getLogger()
F_MAX = [4, 1.5, 1.0, 0.8]
F_VAR = [2.5, 0.5, 0.2, 0.2]
SAMPLE_THRESHOLDS = [20_000, 60_000, 70_000, 80_000]
PIG_IRON_BASE_PRICE = 0.44000003


def get_price(
    stock: int, buy_amount: int, thresholds: list[int], base_price: float
) -> float:
    if buy_amount > stock:
        raise Exception(f"buy_amount {buy_amount} > stock {stock}")
    price = 0
    interval = 0
    remaining = stock - buy_amount
    LOGGER.debug(f"get_price for {buy_amount} of {stock} ({remaining} remaining)")
    while interval < 4:
        if remaining < thresholds[interval]:
            # Remaining is smaller than the end of the threshold bracket, therefore we are buying from it
            interval_start = 0 if interval == 0 else thresholds[interval - 1]
            interval_end = thresholds[interval]
            interval_size = interval_end - interval_start
            w_interval_stock = min(stock, interval_end)  # Smaller of stock and interval
            w_relative_stock = (
                w_interval_stock - interval_start
            )  # Distance of stock from start of interval

            # Get the amount in the current bracket (i.e. everything until the next threshold or stock)
            w_b = w_interval_stock - max(remaining, interval_start)
            w_relative_remain = w_relative_stock - w_b

            new_bracket_stock = w_interval_stock - w_b
            # f = get_factor2(interval, interval_stock, new_bracket_stock, thresholds)
            f = get_factor(interval, w_relative_stock, w_relative_remain, interval_size)
            LOGGER.debug(f"{w_interval_stock} {new_bracket_stock} {f}")
            bracket_price = base_price * w_b * f
            LOGGER.debug(
                f"Buying {w_b} below in {interval} with f={f} for {bracket_price} ({w_relative_remain} remaining)"
            )
            price += bracket_price

            if stock <= interval_end:
                break
        interval += 1

    if remaining + buy_amount > thresholds[3]:
        interval_start = thresholds[3]
        interval_end = stock
        w_b = interval_end - max(remaining, interval_start)
        f = 0.6
        LOGGER.debug(f"Buying {w_b} above t3 with f={f}")
        price += base_price * w_b * f

    return price


def get_factor(
    interval: int, w_relative_stock: int, w_relative_remain: int, interval_width: int
) -> int:
    LOGGER.debug(
        f"get_factor(interval={interval}, w_interval_stock={w_relative_stock}, w_relative_remain={w_relative_remain})"
    )
    if interval == 4:
        return 0.6
    else:
        middle = (w_relative_stock + w_relative_remain) / 2
        return F_MAX[interval] - F_VAR[interval] * (middle) / (interval_width)


def plot_example1():
    plt.clf()
    params = {"mathtext.default": "regular"}
    plt.rcParams.update(params)
    fig, (ax1) = plt.subplots(1, 1)
    x = []
    t0_f_y = []
    t0_pigiron_y = []
    for stock in range(2000, SAMPLE_THRESHOLDS[-1] + 10_000):
        # for stock in range(17000, 23000):
        x.append(stock)
        t0_pigiron_y.append(
            get_price(stock, 2000, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
        )
        if len(t0_pigiron_y) > 2 and t0_pigiron_y[-1] > t0_pigiron_y[-2]:
            raise Exception(f"At {stock} stock, we have an increase in price")

    ax1.plot(x, t0_pigiron_y)

    ax1.axvline(SAMPLE_THRESHOLDS[0])
    ax1.annotate("$t_0$", xy=(SAMPLE_THRESHOLDS[0], ax1.get_ylim()[1]), xycoords='data', xytext=(2, -10), textcoords='offset points')
    ax1.axvline(SAMPLE_THRESHOLDS[1])
    ax1.annotate("$t_1$", xy=(SAMPLE_THRESHOLDS[1], ax1.get_ylim()[1]), xycoords='data', xytext=(2, -10), textcoords='offset points')
    ax1.axvline(SAMPLE_THRESHOLDS[2])
    ax1.annotate("$t_2$", xy=(SAMPLE_THRESHOLDS[2], ax1.get_ylim()[1]), xycoords='data', xytext=(2, -10), textcoords='offset points')
    ax1.axvline(SAMPLE_THRESHOLDS[3])
    ax1.annotate("$t_3$", xy=(SAMPLE_THRESHOLDS[3], ax1.get_ylim()[1]), xycoords='data', xytext=(2, -10), textcoords='offset points')

    ax1.axhline(PIG_IRON_BASE_PRICE * 2000)
    ax1.annotate("Base Price", xy=(0, PIG_IRON_BASE_PRICE * 2000), xycoords='data', xytext=(2, -10), textcoords='offset points')

    ax1.set_title("Buying Price of 1 Pigiron Bundle")
    ax1.set_xlabel("Stock")
    ax1.set_ylabel("Price")

    plt.tight_layout()
    plt.savefig("buying-price-pigiron.png", dpi=150)


def plot_factor():
    plt.clf()
    params = {"mathtext.default": "regular"}
    plt.rcParams.update(params)
    fig, (ax1) = plt.subplots(1, 1)

    # Intervals
    left = 0
    for i in range(0, len(SAMPLE_THRESHOLDS)):
        t = SAMPLE_THRESHOLDS[i]
        bar = ax1.barh(0, t - left, 1, left=left, label=f"Interval {i}")
        left += t - left

    # Stock
    stock = 50_000
    ax1.barh(-1, stock, 1, label=f"Stock")

    # Buying
    buy = 20_000
    ax1.barh(-2, buy, 1, left=stock - buy, label=f"Buy")

    ax1.barh(
        -3,
        stock - SAMPLE_THRESHOLDS[0],
        1,
        left=SAMPLE_THRESHOLDS[0],
        label=f"Relative Stock",
    )
    ax1.barh(
        -4,
        stock - buy - SAMPLE_THRESHOLDS[0],
        1,
        left=SAMPLE_THRESHOLDS[0],
        label=f"Relative Remain",
    )

    ax1.set_yticks(
        [0, -1, -2, -3, -4],
        labels=["Intervals", "Stock", "Buy", "Relative Stock", "Relative Remain"],
    )
    ax1.set_ylim([-10, 1.5])
    plt.tight_layout()
    plt.savefig("buying-price-factor.png", dpi=200)


def tests():
    stock = 2_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(3410.000212490559)

    stock = 4_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(3190.00019878149)

    stock = 18_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(1649.999995396131)

    stock = 23_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(1298.000080883503)

    stock = 23_000
    buy_amount = 5 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(7922.750493697822)

    stock = 55_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(946.0000589489937)

    stock = 65_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(809.6001041603122)

    stock = 75_000
    buy_amount = 1 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(633.6000931930575)

    stock = 110_000
    buy_amount = 50 * 2000
    price = get_price(stock, buy_amount, SAMPLE_THRESHOLDS, PIG_IRON_BASE_PRICE)
    assert price == pytest.approx(46310.00288575888)


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
tests()
plot_example1()
plot_factor()


stock = 6600
buy_amount = 1 * 200
t2 = [1000, 2000, 3000, 4000]
price = get_price(stock, buy_amount, t2, 1.4)
print(price)
