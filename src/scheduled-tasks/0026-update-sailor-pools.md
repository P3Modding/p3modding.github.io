# Update Sailor Pools
The `st_update_sailor_pools` function at `0x004F6C10` updates all sailor pools of all merchants.
The pool size is calulated with the following formula:
```python
increase = sailor_reputation // 4
beggar_multiplier = min(100, town.beggars)

new_value = merchant.sailor_pools[town_index] + increase
capped_value = (beggar_multiplier * sailor_reputation) // 20

merchant.sailor_pools[town_index] = min(new_value, capped_value)
```
The pool size cannot exceed `capped_value`, which cannot exceed `(100*20)//20`, so the pool size is capped at `100`.
Merchants cannot hire any sailors while their sailor reputation is below `4`, because `increase` will be `0`.

## Interval
This scheduled task reschedules itself 64 ticks ahead, so it is executed at tick 0, 64, 128, and 192 every day.
