# Excess Consumption
The `town_excess_consumption` function at `0x00528630` reduces excess wares which cannot be produced in the town.
It is called in `town_tick` if the town is not under siege.

## Calculation
```python
def calculate_excess_consumption(
    daily_production: int,
    daily_consumption_citizens: int,
    daily_consumption_businesses: int,
    current_amount: int,
    t1: int,
    t3: int,
) -> int:
    if daily_production:
        return 0
    if current_amount <= t1:
        return 0

    above_t1 = current_amount - t1
    consumption = daily_consumption_citizens + daily_consumption_businesses
    removed_amount = above_t1
        * 16
        * consumption
        // 10
        // t3

    return min(removed_amount, above_t1)
```
