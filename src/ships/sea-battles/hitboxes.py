import matplotlib.pyplot as plt
import numpy as np


snaikka_x = [-19, 0, 19, 19, -19]
snaikka_y = [-31, -55, -31, 47, 47]
crayer_x = [-21, 0, 21, 19, -19]
crayer_y = [-36, -66, -36, 55, 55]
cog_x = [-25, 0, 25, 19, -19]
cog_y = [-14, -54, -14, 67, 67]
holk_x = [-22, 0, 22, 19, -19]
holk_y = [-25, -67, -25, 81, 81]


def complete_hitbox_plot_data(data: list[int]):
    return data + [data[0]]


plt.figure(figsize=(10, 8))
plt.plot(
    complete_hitbox_plot_data(snaikka_x),
    complete_hitbox_plot_data(snaikka_y),
    label="Snaikka",
)
plt.plot(
    complete_hitbox_plot_data(crayer_x),
    complete_hitbox_plot_data(crayer_y),
    label="Crayer",
)
plt.plot(
    complete_hitbox_plot_data(cog_x), complete_hitbox_plot_data(cog_y), label="Cog"
)
plt.plot(
    complete_hitbox_plot_data(holk_x), complete_hitbox_plot_data(holk_y), label="Holk"
)
plt.legend(loc="best")
plt.gca().set_aspect("equal")
plt.savefig("hitboxes.png", dpi=200)
