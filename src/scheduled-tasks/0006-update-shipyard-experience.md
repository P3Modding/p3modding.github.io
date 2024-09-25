# Update Shipard Experience
The `st_update_shipyard_experience` function at `0x004E2144` updates the experience, utilization markups and ship quality levels of all shipyards.

## Pending Experiene and Utilization Markup
Pending experience is added to the shipyard's experience and set to `0`.
The utilization is updated as follows:
```python
capacity = 0
for ship_order in ship_orders:
    capacity += ship_order.capacity

markup_change = (capacity // 2000 + pending_experience // 19600) / 26
utilization_markup = markup_change + utilization_markup * 0.96153843
```

## Unlocking Ship Quality Levels
The `shipyard_level_requirements` table at `0x00673818` defines the following *base experience requirements*:

|Type|QL 0|QL 1|QL 2|QL 3|
|-|-|-|-|-|
|Snaikka|0|100|300|1050|
|Crayer|0|100|600|900|
|Cog|0|200|400|800|
|Holk|300|500|600|1200|

A new quality level is unlocked, if the shipyard's experience exceeds `2800 * required_base_experience`.

## Interval
This scheduled task reschedules itself 0x700 ticks ahead, so it is executed once per week.
