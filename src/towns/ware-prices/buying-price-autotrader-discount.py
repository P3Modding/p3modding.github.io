import logging
from matplotlib import pyplot as plt


def calculate_discount(xp: int):
    return 100 - (2 * (50 - xp // 43))


LOGGER = logging.getLogger()
plt.clf()
plt.title("Auto Trader Discount")
plt.xlabel("Experience")
plt.ylabel("Discount (Percent)")

x_data = []
y_data = []
for i in range(0, 251):
    x_data.append(i)
    y_data.append(calculate_discount(i))

plt.plot(x_data, y_data)
plt.savefig("buying-price-autotrader-discount.png", dpi=200)
