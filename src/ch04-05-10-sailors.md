# Sailors
Sailors are recruited from beggars.
The "sailors" page is only available if at least one sailor can be hired.

## Sailor Pools
The merchant struct's `sailor_pools` array at offset `0xf0` contains an `u8` for every town (indexed by the town's index), which denotes the size of the sailor pool of the merchant in that town.

The scheduled task `update_sailor_pools` updates all sailor pools of one merchant.
The pool size is calulated with the following formula:
```python
increase = sailor_reputation // 4
beggar_multiplier = min(100, town.beggars)

new_value = merchant.sailor_pools[town_index] + increase
capped_value = (beggar_multiplier * sailor_reputation) // 20

merchant.sailor_pools[town_index] = min(new_value, capped_value)
```
The pool size cannot exceed `capped_value`, which cannot exceed `(100*20)//20`, so the pool size is capped at `100`.
Consequently, the pool sizes are set to `0` if the sailor reputation is `0`.
Merchants cannot hire any sailors while their sailor reputation is below `4`, because `increase` will be `0`.

## Hiring Sailors
The amount of sailors that can be hired is determined by the `get_available_sailors` function at `0x004F6CA0`.
It implements the following formula:
```python
hirable_sailors = min(0, town.beggars - 1, merchant.sailor_pools[town_index])
```

## UI Limits
If `get_available_sailors` returns an amount higher than `50`, the UI caps the amount of hirable sailors in a single transaction.
