import matplotlib.pyplot as plt
import numpy as np

X_RANGE = range(1, 600)

damage1 = [
    0x20,
    0x20,
    0x4D,
    0x4D,
    0x60,
    0x3A,
]

damage2 = [
    0x3C,
    0x50,
    0x3C,
    0x50,
    0x5A,
    0x5A,
]

reduction = [
    0x1E0,
    0xA0,
    0x1E0,
    0xA0,
    0x78,
    0x78,
]

artillery_names = [
    "Small Catapult",
    "Small Ballista",
    "Large Catapult",
    "Large Ballista",
    "Bombard",
    "Cannon",
]

slot_adjustment = [
    1,
    1,
    0.5,
    0.5,
    0.5,
    1,
    1,
]


def calc_raw_damage(distance, artillery_type):
    return max(
        0,
        distance
        * damage1[artillery_type]
        * damage2[artillery_type]
        // (-6 * reduction[artillery_type])
        + damage1[artillery_type] * damage2[artillery_type],
    )


def calc_scaled_damage(raw_damage):
    return 2800 * (raw_damage // 64) // 100


def apply_captain_factor(scaled_damage: int, combat_experience: int):
    if not combat_experience:
        return scaled_damage
    else:
        return scaled_damage * (6 * combat_experience // 17 + 100) // 100


def apply_difficulty_and_maintenance(
    damage: int, difficulty: int, ship_maintenance: int, is_ai: bool
):
    f = min(4, max(ship_maintenance >> 8, 0))
    if not is_ai:
        match difficulty:
            case 0:  # Easy
                f += 2
            case 2:  # Hard
                f -= 2
    if f > 0:
        return damage + damage * (f - 2) // 20
    else:
        return damage + damage * (f - 1) // 20


def plot_raw():
    plt.clf()
    plt.title("Raw Damage per Slot")
    plt.xlabel("Distance")
    plt.ylabel("Damage")
    x_data = []
    for x in X_RANGE:
        x_data.append(x)

    for artillery_type in reversed(range(6)):
        y_data = []
        for x in X_RANGE:
            y_data.append(
                calc_raw_damage(x, artillery_type) * slot_adjustment[artillery_type]
            )
        plt.plot(x_data, y_data, label=artillery_names[artillery_type], linewidth=1)

    plt.legend(loc="upper right")
    plt.savefig("damage_raw.png", dpi=200)


def plot_scaled():
    plt.clf()
    plt.title("Scaled Damage per Slot")
    plt.xlabel("Distance")
    plt.ylabel("Damage")
    x_data = []
    for x in X_RANGE:
        x_data.append(x)

    for artillery_type in reversed(range(6)):
        y_data = []
        for x in X_RANGE:
            y_data.append(
                calc_scaled_damage(calc_raw_damage(x, artillery_type))
                * slot_adjustment[artillery_type]
            )
        plt.plot(x_data, y_data, label=artillery_names[artillery_type], linewidth=1)

    plt.legend(loc="upper right")
    plt.savefig("damage_scaled.png", dpi=200)


def plot_captain():
    plt.clf()
    plt.title("Scaled Damage per Slot with Captains")
    plt.xlabel("Distance")
    plt.ylabel("Damage")
    x_data = []
    for x in X_RANGE:
        x_data.append(x)

    for captain_combat_experience in [0, 50, 100, 150, 200, 250]:
        y_data = []
        for x in X_RANGE:
            y_data.append(
                apply_captain_factor(
                    calc_scaled_damage(calc_raw_damage(x, 5)) * slot_adjustment[5],
                    captain_combat_experience,
                )
            )
        plt.plot(
            x_data,
            y_data,
            label=artillery_names[5] + f" ({captain_combat_experience} XP)",
            linewidth=1,
        )

    plt.legend(loc="upper right")
    plt.savefig("damage_captain.png", dpi=200)


if __name__ == "__main__":
    plot_raw()
    plot_scaled()
    plot_captain()
