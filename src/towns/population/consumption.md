# Consumption
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
**TODO clarify**
**TODO pitch consumption (sieged and unsieged), winter/famine/plague modifiers**
