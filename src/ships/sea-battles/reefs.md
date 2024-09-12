# Reefs
The `tick_sea_battle_object_pair` function at `0x00608850` applies the following damage to a ship on a reef:

```python
def calc_reef_damage(ship_speed: int):
    return ship_speed // 1024
```

Reefs don't kill sailors or artillery pieces.
