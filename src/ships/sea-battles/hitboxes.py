import matplotlib.pyplot as plt
import numpy as np
from labellines import labelLines
from math import sin, cos, pi


snaikka_x = [-19, 0, 19, 19, -19]
snaikka_y = [-31, -55, -31, 47, 47]
crayer_x = [-21, 0, 21, 19, -19]
crayer_y = [-36, -66, -36, 55, 55]
cog_x = [-25, 0, 25, 19, -19]
cog_y = [-14, -54, -14, 67, 67]
holk_x = [-22, 0, 22, 19, -19]
holk_y = [-25, -67, -25, 81, 81]
rotated_crayer_x = [3, -17, 18, 103, 89]
rotated_crayer_y = [-2, -32, -41, -6, 29]


def complete(data: list[int]):
    return data + [data[0]]


def get_annotation(box_coord: int):
    if box_coord == 0 or box_coord == 4:
        return f"left"
    if box_coord == 1 or box_coord == 2:
        return f"right"
    if box_coord == 0 or box_coord == 3:
        return f"random"


def get_color(box_coord: int):
    if box_coord == 0 or box_coord == 4:
        return f"r"
    if box_coord == 1 or box_coord == 2:
        return f"g"
    if box_coord == 0 or box_coord == 3:
        return f"b"


def rot_x(x, y, r):
    return x * cos(r) - y * sin(r)


def rot_y(x, y, r):
    return x * sin(r) + y * cos(r)


plt.gca().invert_yaxis()
plt.plot(
    complete(snaikka_x),
    complete(snaikka_y),
    label="Snaikka",
)
plt.plot(
    complete(crayer_x),
    complete(crayer_y),
    label="Crayer",
)
plt.plot(complete(cog_x), complete(cog_y), label="Cog")
plt.plot(complete(holk_x), complete(holk_y), label="Holk")
plt.legend(loc="best")
plt.gca().set_aspect("equal")
plt.savefig("hitboxes.png", dpi=200)


SHIP_X = 100
SHIP_Y = 100
SHIP_DIRECTION_1 = 0
SHIP_DIRECTION_2 = pi / 8
PROJECTILE_X_1 = 50
PROJECTILE_Y_1 = 50
PROJECTILE_X_2 = 140
PROJECTILE_Y_2 = 130
plt.clf()
fig, axs = plt.subplots(1, 2)
# Left
axs[0].invert_yaxis()
axs[0].xaxis.tick_top()
axs[0].set_adjustable("datalim")
axs[0].set_aspect("equal")
axs[0].set_title("Sea Battle Coordinates")
axs[0].plot(
    PROJECTILE_X_2,
    PROJECTILE_Y_2,
    marker="o",
    markersize=7,
    markeredgecolor="red",
    markerfacecolor="red",
)

for i in range(5):
    axs[0].plot(
        [
            rot_x(crayer_x[i - 1 % 5], crayer_y[i - 1 % 5], SHIP_DIRECTION_2) + SHIP_X,
            rot_x(crayer_x[i], crayer_y[i], SHIP_DIRECTION_2) + SHIP_X,
        ],
        [
            rot_y(crayer_x[i - 1 % 5], crayer_y[i - 1 % 5], SHIP_DIRECTION_2) + SHIP_Y,
            rot_y(crayer_x[i], crayer_y[i], SHIP_DIRECTION_2) + SHIP_Y,
        ],
        "b",
    )
# Right
axs[1].invert_yaxis()
axs[1].xaxis.tick_top()
axs[1].set_adjustable("datalim")
axs[1].set_aspect("equal")
axs[1].set_title("Projectile-Centric Coordinates")
axs[1].plot(
    0, 0, marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red"
)
for i in range(5):
    axs[1].plot(
        [
            rot_x(crayer_x[i - 1 % 5], crayer_y[i - 1 % 5], SHIP_DIRECTION_2)
            + SHIP_X
            - PROJECTILE_X_2,
            rot_x(crayer_x[i], crayer_y[i], SHIP_DIRECTION_2) + SHIP_X - PROJECTILE_X_2,
        ],
        [
            rot_y(crayer_x[i - 1 % 5], crayer_y[i - 1 % 5], SHIP_DIRECTION_2)
            + SHIP_Y
            - PROJECTILE_Y_2,
            rot_y(crayer_x[i], crayer_y[i], SHIP_DIRECTION_2) + SHIP_Y - PROJECTILE_Y_2,
        ],
        "b",
    )
fig.align_titles()
fig.tight_layout()
plt.savefig("hitboxes_transformation.png", dpi=200)


plt.clf()
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.gca().set_adjustable("datalim")
plt.gca().set_aspect("equal")
plt.gca().set_title("Hitbox Impact Location Mapping")
plt.scatter(crayer_x, crayer_y, label="Crayer")
for i in range(5):
    plt.annotate(f"{i}", (crayer_x[i] + 3, crayer_y[i] - 1))
for i in range(5):
    plt.plot(
        [crayer_x[i - 1 % 5], crayer_x[i]],
        [crayer_y[i - 1 % 5], crayer_y[i]],
        get_color(i),
        label=f"{get_annotation(i)}",
    )
labelLines(
    plt.gca().get_lines(),
    align=False,
    xvals=[(x + crayer_x[(i - 1) % 5]) / 2 for i, x in enumerate(crayer_x)],
)
fig.align_titles()
fig.tight_layout()
plt.savefig("hitboxes_impact_location.png")
