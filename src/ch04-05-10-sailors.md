# Sailors
Sailors are recruited from beggars.
The "Sailors" page is only available if at least one sailor can be hired.

## Sailor Pools
The merchant struct's `sailor_pools` array at offset `0xf0` contains an `u8` for every town (indexed by the town's index), which denotes the size of the sailor pool of the merchant in that town.

## Hiring Sailors
The amount of sailors that can be hired is determined by the `get_available_sailors` function at `0x004F6CA0`.
It implements the following formula:
```python
hirable_sailors = min(0, town.beggars - 1, merchant.sailor_pools[town_index])
```

## UI Limits
If `get_available_sailors` returns an amount higher than `50`, the UI caps the amount of hirable sailors in a single transaction.
