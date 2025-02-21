import matplotlib.pyplot as plt
import numpy as np


def is_upgrade_approved(rank: int, total_citizens: int, old_approved_size: int, under_siege: bool) -> bool:
    no = 22
    # Assuming no bribes
    # Assuming singleplayer
    if rank == 4:
        no -= 1 # Councillor
    elif rank == 5:
        no -= 2 # Patrician
    else:
        no -= 3 # Mayor/Alderman

    if under_siege:
        total_citizens *= 2

    t = 512 - 203 * old_approved_size + total_citizens
    if t < 100:
        yes = no // 10
    elif t <= 920:
        yes = no * t >> 10
    else:
        yes = 9 * no // 10
    no -= yes
    
    if rank == 4:
        yes += 1
    else:
        yes += 3

    return yes > no


def plot_approved_limit_per_citizens():
    plt.clf()
    plt.title("Militia Expansion Votes (Singleplayer, Alderman, No Bribes)")
    plt.xlabel("Total Citizens")
    plt.ylabel("Approved Size")
    x_data = []
    y_data = []

    for x in range(1_000, 6_000):
        x_data.append(x)
        for old_approved_size in range(1, 100).__reversed__():
            if is_upgrade_approved(7, x, old_approved_size, False):
                y_data.append(old_approved_size)
                break


    plt.plot(x_data, y_data, linewidth=1)
    plt.savefig("002e-council-meeting-approved-limits.png", dpi=200)


plot_approved_limit_per_citizens()
