# Shipyard

## Shipbuilding
The `handle_build_ship` function is at `0x0052A360`.

### Quality Levels
A shipyard's current quality level of each ship type is stored in the town's current ship level array, indexed by the ship type.
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
capacity = 2000 * structure_value
health = 2800 * structure_value
```
For a QL 3 hulk, this yields the expected capacity of 140.000 (700 barrels).


### Resources and Price
The `calculate_ship_build_cost` function is at `0x0052B2C0`.
At `0x0066DEB0` there is a table that contains the requirements of every ship type and quality level, capped at QL 2 (QL 3 does not increase cost):

|Type|QL|Timber|Cloth|Hemp|Pitch|Iron Goods|Unknown|Base Price|Unknown|
|-|-|-|-|-|-|-|-|-|-|
|Snaikka|0|7|3|3|3|20|17|7.650|11.414|
|Snaikka|1|9|3|3|3|20|20|8.200|12.074|
|Snaikka|2|11|3|3|3|20|24|8.800|12.784|
|Craier|
|Cog|
|Hulk|

## Repairs

## Upgrade Levels
