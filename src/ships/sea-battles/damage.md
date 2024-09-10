# Damage
A projectile's damage primarily depends on the distance, but also some other factors.
The code for all plots can be found [here](./damage.py).

## Range
The *raw damage* of a projectile is controlled through 3 tables: Damage Component 1 at `0x00672CC0`, Damage Component 2 at `0x00672CD0`, and Damage Reduction at `0x00672CE4`.
The vanilla values are shown in the following table:

|Artillery Type|Damage 1|Damage 2|Damage Reduction|
|-|-|-|-|
|Small Catapult|32|60|480|
|Small Ballista|32|80|160|
|Large Catapult|77|60|480|
|Large Ballista|77|80|160|
|Bombard|96|90|120|
|Cannon|58|90|120|

The formula of the raw damage is as follows:
```python
def calc_raw_damage(distance: int, artillery_type: int):
    return max(0, distance \
            * damage1[artillery_type] \
            * damage2[artillery_type] \
            // (-6 * reduction[artillery_type]) \
        + \
            damage1[artillery_type] \
            * damage2[artillery_type])
```

The following image shows the plot of raw damage and distance, with the damage values of double slot weapons adjusted by `0.5`.
![image](damage_raw.png)

## Scaling
The raw damage is scaled linearly:
```python
def calc_scaled_damage(raw_damage: int):
    return 2800 * (raw_damage // 64) // 100
```

The precision loss caused by the division by 64 has a slight effect on the granularity:
![image](damage_scaled.png)

## Captain
The captain's combat experience (a value between `0` for a combat level `0` and `250` for a combat level `5` captain) increases the damage:

```python
def apply_captain_factor(scaled_damage: int, combat_experience: int):
    if not combat_experience:
        return scaled_damage
    else:
        return scaled_damage * (6 * combat_experience // 17 + 100) // 100
```
This factor is roughly (ignoring precision loss through divisions) equivalent to \\(\frac{3 * combat\\_experience}{850} + 1\\) or \\(0.17647058823 * combat\\_level + 1\\).
The following figure highlights the impact of a captain on a projectile's damage:
![image](damage_captain.png)

## Difficulty and Maintenance
The sea battle difficulty setting and the ship's current maintenance value affect the damage as follows:
```python
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
```
Since `f` cannot exceed `6`, the bonus damage from difficulty and maintenance will not exceed \\(\frac{1}{5} * damage \\).

## Normal Distribution and Minimum
Finally, a factor with a discrete uniform (assuming the sea battle's PRNG works as intended) distribution in the discrete (up to the second decimal point) interval from `0.85` to `1.15` is applied, and a minimum damage of `1` is enforced:
```python
# Discrete distribution
damage = damage * (battle_rand() % 31 + 85) // 100

# Minimum
damage = max(damage, 1)
```

## Sailor Damage
Damage to sailors is calculated as follows:
```python
def calc_killed_sailors(
    sailors: int,
    damage: int,
    rng: int,
    pending_sailor_damage: int,
    ship_max_hp: int
) -> Tuple[int, int]:
    sailor_damage_rng = (rng & 0x400) + 3072 # 3072 or 4096
    scaled_sailor_damage = (sailors + 1) * sailor_damage_rng
    final_sailor_damage = pending_sailor_damage + scaled_sailor_damage / (ship_max_hp // 16)
    killed_sailors = final_sailor_damage >> 16
    new_pending_sailor_damage = final_sailor_damage & 0xffff
    return killed_sailors, new_pending_sailor_damage
```
