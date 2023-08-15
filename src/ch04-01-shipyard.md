# Shipyard

## Shipbuilding
The `handle_build_ship` function is at `0x0052A360`.

### Build Capabilities
A shipyard's current quality level of each ship type is stored in the town's current *ship quality level* array, indexed by the ship type.
The `u8` values range from 0 to 3.

### HP and Capacity
A ship's HP and capacity depend on the respective quality level.
At `0x00673838` there is a table that holds the *structure base values* for every ship type and quality level:

|Type|Quality Level 0|Quality Level 1|Quality Level 2|Quality Level 3|
|-|-|-|-|-|
|Snaikka|15|19|23|25|
|Craier|28|31|34|35|
|Cog|45|48|52|55|
|Hulk|55|59|65|70|

To the structure base value an unknown value is added, which appears to be always zero. The resulting structure value is capped at the value of QL 3.

HP and Capacity scale linearly with the structure value:
```
capacity = 2000 * structure_base_value
health = 2800 * structure_base_value
```
For a QL 3 hulk, this yields the expected capacity of 140.000 (700 barrels).


### Resources and Price
The `calculate_ship_build_cost` function is at `0x0052B2C0`.
The shipyard charges a *utilization markup* that increases when the shipyard is in use, and decreases if it is not.
At `0x0066DEB0` there is a table that contains the requirements of every ship type and quality level, capped at QL 2 (QL 3 does not increase cost):

|Type|QL|Timber|Cloth|Hemp|Pitch|Iron Goods|Unknown|Base Price|Unknown|
|-|-|-|-|-|-|-|-|-|-|
|Snaikka|0|7|3|3|3|20|17|7,650|11,414|
|Snaikka|1|9|3|3|3|20|20|8,200|12,074|
|Snaikka|2|11|3|3|3|20|24|8,800|12,784|
|Craier|0|12|5|5|5|30|29|18,260|24,450|
|Craier|1|14|5|5|5|30|32|18,720|25,010|
|Craier|2|16|5|5|5|30|34|19,890|26,290|
|Cog|0|18|3|4|4|40|46|16,560|22,296|
|Cog|1|20|3|4|4|40|50|16,500|22,346|
|Cog|2|22|3|4|4|40|53|17,490|23,446|
|Hulk|0|30|16|16|8|50|58|22,968|34,442|
|Hulk|1|33|16|16|8|50|64|23,040|34,579|
|Hulk|2|36|16|16|8|50|69|24,840|36,664|

Wares are consumed as listed in the table.
The ship price is calculated as follows:

```
def structure_markup(structure):
    if structure < 20:
        return 900
    if structure < 30:
        return 840
    if structure < 40:
        return 780
    if structure < 50:
        return 720
    if structure < 60:
        return 660
    else:
        return 600

price = base_price
    + structure_markup(structure_base_value)
    + utilization_markup
```

## Repairs

## Upgrade Levels
