# Celebration
The `st_celebration` function is at `0x004E23A4`.

```
00000000 struct scheduled_task_celebration // sizeof=0x10
00000000 {
00000000     signed __int32 field_0_merchant_index;
00000004     signed __int32 field_4_town_index;
00000008     signed __int32 field_8_maybe_type;
0000000C     signed __int32 field_C;
00000010 };
```

## Consumption
The `celebration_base_consumption` table at `0x006734E8` defines the base consumption per guest:

|Ware|Base Consumption|
|-|-|
|Grain|3|
|Meat|2|
|Fish|2|
|Beer|2|
|Salt|0|
|Honey|1|
|Spices|0|
|Wine|2|

The consumption per guest is calculated as follows:
```python
celebration_wares = [
    WareId.Grain,
    WareId.Meat,
    WareId.Fish,
    WareId.Beer,
    WareId.Salt,
    WareId.Honey,
    WareId.Spices,
    WareId.Wine,
]

for ware in celebration_wares:
    base_consumption = guests * celebration_base_consumption[ware]
    scaled_consumption = base_consumption * (4 if has_famine else 2)

    # Ceil to the next barrel/bundle
    if is_barrel_ware[ware]:
        consumption = 200 * ((scaled_consumption + 199) / 200)
    else
        consumption = 2000 * ((scaled_consumption + 1999) / 2000)
```

Not having enough wares to cover the **consumption** does not impact celebration level, merchant popularity, or citizen satisfaction.

## Attendance
The amount of guests is calculated as follows:
```python
attendance_ratio = min(99, max(0, 39 + local_reputation))
eligible_citizens = attendance_ratio * total_citizens / 100
satisfied_wares = 0

for ware in celebration_wares:
    if celebration_base_consumption[ware] == 0:
        continue
    if celebration_base_consumption[ware] * eligible_citizens <= office.wares[ware]:
        satisfied_wares += 1

satisfaction_ratio = attendance_ratio * satisfied_wares // 6
capped_satisfaction_ratio = max(2, min(99, satisfaction_ratio))
guests = max(5, total_citizens * capped_satisfaction_ratio // 100)
```

Since exactly 6 wares have a non-zero consumption, `satisfaction_ratio` is equal to `attendance_ratio` if all wares are satisfied.

## Levels
Depending on how many wares were available in sufficient amounts, the celebration is classified as one of the following levels:

|Level|Letter|
|-|-|
|0|This was not really a great celebration [...]|
|1|The celebration was only moderately successful [...]|
|2|The celebration was relatively successful [...]|
|3|It was a fantastic celebration [...]|

A celebration's level is calculated as follows:
```python
level = satisfied_wares // 2
```

Consequently, a partially satisfied ware does not contribute to the celebration's success.

## Satisfaction

## Reputation
Under be assumption that the base_rep_factor is always `1`, the impact of each celebration level is:

|Level|Social Reputation Impact|
|-|-|
|0|-1|
|1|0.5|
|2|1|
|3|1.5|