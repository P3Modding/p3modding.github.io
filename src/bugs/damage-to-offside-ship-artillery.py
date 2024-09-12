import matplotlib.pyplot as plt
import numpy as np
from labellines import labelLines


crayer_x = [-21, 0, 21, 19, -19]
crayer_y = [-36, -66, -36, 55, 55]


def complete_hitbox_plot_data(data: list[int]):
    return data + [data[0]]


def get_annotation(box_coord: int):
    if box_coord == 0 or box_coord == 4:
        return f"{box_coord} (left)"
    if box_coord == 1 or box_coord == 2:
        return f"{box_coord} (right)"
    if box_coord == 0 or box_coord == 3:
        return f"{box_coord} (random)"


def rotate(l: list, n: int):
    return l[n:] + l[:n]


def get_color(box_coord: int):
    if box_coord == 0 or box_coord == 4:
        return f"r"
    if box_coord == 1 or box_coord == 2:
        return f"g"
    if box_coord == 0 or box_coord == 3:
        return f"b"

'''
plt.clf()
plt.figure(figsize=(4, 5))
for i in range(5):
    plt.plot(
        [crayer_x[i-1%5], crayer_x[i]],
        [crayer_y[i-1%5], crayer_y[i]],
        label=f"{get_annotation(i)}")
plt.gca().set_aspect("equal")
labelLines(plt.gca().get_lines(), align=False, xvals=[(x+crayer_x[(i-1)%5])/2 for i, x in enumerate(crayer_x)])
plt.margins(x=0.4,y=0.1)
plt.savefig("damage-to-offside-ship-artillery_hitbox.png", dpi=100)


plt.clf()
plt.figure(figsize=(4, 5))
for i in range(5):
    plt.plot(
        [rotate(crayer_x, 1)[i-1%5], rotate(crayer_x, 1)[i]],
        [rotate(crayer_y, 1)[i-1%5], rotate(crayer_y, 1)[i]],
        label=f"{get_annotation(i)}")
plt.gca().set_aspect("equal")
labelLines(plt.gca().get_lines(), align=False, xvals=[(x+rotate(crayer_x, 1)[(i-1)%5])/2 for i, x in enumerate(rotate(crayer_x, 1))])
plt.margins(x=0.4,y=0.1)
plt.savefig("damage-to-offside-ship-artillery_hitbox-fixed.png", dpi=100)
'''

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
plt.tight_layout()
plt.savefig("damage-to-offside-ship-artillery_hitbox.png")

plt.clf()
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.gca().set_adjustable("datalim")
plt.gca().set_aspect("equal")
plt.gca().set_title("Fixed Hitbox Impact Location Mapping")
plt.scatter(rotate(crayer_x, 1), rotate(crayer_y, 1), label="Crayer")
for i in range(5):
    plt.annotate(f"{i}", (rotate(crayer_x, 1)[i] + 3, rotate(crayer_y, 1)[i] - 1))
for i in range(5):
    plt.plot(
        [rotate(crayer_x, 1)[i - 1 % 5], rotate(crayer_x, 1)[i]],
        [rotate(crayer_y, 1)[i - 1 % 5], rotate(crayer_y, 1)[i]],
        get_color(i),
        label=f"{get_annotation(i)}",
    )
labelLines(
    plt.gca().get_lines(),
    align=False,
    xvals=[(x + rotate(crayer_x, 1)[(i - 1) % 5]) / 2 for i, x in enumerate(rotate(crayer_x, 1))],
)
plt.tight_layout()
plt.savefig("damage-to-offside-ship-artillery_hitbox_fixed.png")
