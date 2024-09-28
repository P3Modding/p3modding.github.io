# Impact
Once the `get_sea_battle_projectile_impact_direction` at `0x0060A73C` has detected an impact, the projectile's damage is applied, and the object is freed.
Projectiles can deal damage to a ship's HP, sailors and artillery.

## HP Damage
The projectile's damage value is subtracted from its hitpoints, and the ship is killed if they drop to or below `0`.

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

## Ship Artillery Slot Damage
