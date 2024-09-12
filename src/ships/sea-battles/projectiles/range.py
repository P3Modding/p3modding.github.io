import math
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


def calc_max_distance(relative_angle: int):
    if relative_angle >= 0x80:
        bonus_range_factor = 0xC0 - relative_angle
    else:
        bonus_range_factor = relative_angle - 0x40

    return bonus_range_factor * 4320 // 3200 + 480


CENTER_X = 0
CENTER_Y = 0
data = []
ship_direction = 0
for relative_angle in range(0, 0x101):
    if relative_angle % 8 == 0:
        max_distance = calc_max_distance(relative_angle)
        data.append([relative_angle * 1.40625, max_distance])

xs, ys = zip(*data)

plt.title("Wind Impact on Artillery Range")
plt.xlabel("Ship Wind Angle (°)")
plt.ylabel("Maximum Range")
plt.xticks(range(0, 360 + 45, 45), labels=range(0, 360 + 45, 45))
plt.plot(xs, ys)
plt.plot([0, 360], [480, 480])
plt.savefig("range_relative.png", dpi=200)
