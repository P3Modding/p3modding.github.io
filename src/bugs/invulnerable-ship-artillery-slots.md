# Invulnerable Ship Artillery Slots Bug
<p style="text-align:center">
    <img src="invulnerable-ship-artillery-slots.png">
</p>

## Summary
The `apply_sea_battle_damage` function at `0x0061F96F` never destroys the artillery in the first two slots.

## Details
The starting index of the loops over the artillery slots is too high to cover the first two slots.
It is calculated as follows:
```python
if impact_location == 3: # random
    slot_pattern = (get_battle_rand() & 1) + 1 # 1 or 2
elif impact_location == 1: # left
    slot_pattern = 2
elif impact_location == 2: # right
    slot_pattern = 1

i = slot_pattern * 2
```
Consequently, for a hit to the left side `i` is initialized to 4, which makes the slots 0 and 1 invulnerable.

## Fix
To fix the issue, the index calculation must be changed to yield [0 for the left side](https://github.com/P3Modding/p3-lib/tree/master/mod-fix-invulnerable-ship-artillery-slots).
