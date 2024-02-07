# Population

## Consumption
The `do_population_consumption` function is at `0x00527D40`.

At `0x00672860` there is a table that contains the daily consumptions for 100 citizens of every population type:

|Ware|Rich|Wealthy|Poor|Beggars|
|-|-|-|-|-|
|Grain|90|120|150|120|
|Meat|110|87|12|5|
|Fish|40|80|100|110|
|Beer|65|130|65|75|
|Salt|1|1|1|1|
|Honey|50|25|5|2|
|Spices|4|2|2|0|
|Wine|150|38|0|0|
|Cloth|50|35|15|1|
|Skins|60|30|0|0|
|WhaleOil|50|35|10|0|
|Timber|80|80|40|20|
|IronGoods|100|75|25|0|
|Leather|44|35|5|0|
|Wool|10|40|20|5|
|Pitch|0|0|0|0|
|PigIron|0|0|0|0|
|Hemp|5|3|2|3|
|Pottery|30|18|12|1|
|Bricks|1|1|0|0|
|Sword|0|0|0|0|
|Bow|0|0|0|0|
|Crossbow|0|0|0|0|
|Carbine|0|0|0|0|

If a town is not under siege and a ware is in oversupply, more of it is consumed.
**TODO pitch consumption (sieged and unsieged), winter/famine/plague modifiers**

## Satisfaction
P3's setting "Needs of the citizens" changes how easy it is to increase the satisfaction, and how fast it changes.
The *satisfaction classes* are displayed in-game: *Very happy*, *happy*, *very satisfied*, *satisfied*, *dissatisfied*, and *annoyed*.
The satisfaction for each population type is stored in the town's *satisfactions* array, holding an `i16` for every population type except Beggars.
The function `prepare_citizens_menu_ui` at `0x0040B570` calculates the satisfaction classes by converting the `i16` into an `f32`, and picking the highest applicable class:

|Satisfaction >|Satisfaction Class|
|-|-|
|29.5|Very Happy|
|19.5|Happy|
|9.5|Very Satisfied|
|0.5|Satisfied|
|-10.5|Dissatisfied|
|-Infinity|Annoyed|

The function `update_citizen_satisfaction` at `0x0051C830` calculates the *current satisfaction* each population type would have.
The satisfaction is then increased or decreaseed by the respective *step size*, depending on whether it was bigger or smaller than the current satisfaction, but it won't go beneath -40 or above 80.
At `0x006736AC` there is a table that contains for every difficulty the step sizes for increments and decrements to the satisfaction:

|Needs Setting|Increment|Decrement|
|-|-|-|
|Low|3|1|
|Normal|2|1|
|High|1|2|
|Unused|1|1|

At `0x006736A0` there is a table that contains for every difficulty the *base satisfaction* for every population type:

|Needs Setting|Rich|Wealthy|Poor|
|-|-|-|-|
|Low|-7|-12|-20|
|Normal|-13|-18|-27|
|High|-20|-25|-32|

Within `update_citizen_satisfaction` 6 *situational modifiers* are implemented:

|Situation|Impact|
|-|-|
|Siege|-10|
|Pirate Attack|-8|
|Plague|-10|
|Blocked|-6|
|Boycotted|-4|
|Famine|-10|

At `0x00672938` there is a table that defines *ware satisfaction weights* for every population type:

|Ware|Rich|Wealthy|Poor|
|-|-|-|-|
|Grain|2|4|8|
|Meat|5|4|4|
|Fish|2|6|6|
|Beer|2|6|6|
|Salt|2|2|4|
|Honey|3|2|0|
|Spices|3|0|0|
|Wine|5|2|0|
|Cloth|5|4|0|
|Skins|3|2|0|
|WhaleOil|3|4|4|
|Timber|3|4|6|
|IronGoods|2|2|0|
|Leather|2|2|4|
|Wool|2|6|4|
|Pitch|0|0|0|
|PigIron|0|0|0|
|Hemp|0|0|0|
|Pottery|3|2|4|
|Bricks|0|0|0|
|Sword|0|0|0|
|Bow|0|0|0|
|Crossbow|0|0|0|
|Carbine|0|0|0|

The current satisfaction is calculated as follows:
```
def get_ware_satisfaction(ware_id, population_type):
    if wares[ware_id] >= 2 * weekly_consumption[ware_id]:
        return satisfaction_weights[population_type][ware_id]
    else:
        return (wares[ware_id] - weekly_consumption[ware_id])
            * satisfaction_weights[population_type][ware_id]
            // weekly_consumption[ware_id]

current_satisfaction = 2 * (
    base_satisfaction
    + situational_modifiers
    + unknown_modifiers # 9 total, 8 capped at 4
    + ware_satisfactions
)
```
