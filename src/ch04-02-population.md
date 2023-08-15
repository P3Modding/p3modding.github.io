# Population

## Consumption

## Satisfaction
P3's setting "Needs of the citizens" changes how easy it is to increase the satisfaction, and how fast it changes.
The *satisfaction classes* are displayed in-game: *Very happy*, *happy*, *very satisfied*, *satisfied*, *dissatisfied*, and *annoyed*.
The satisfaction for each population type is stored in the town's *satisfactions* array, holding an `i16` for every population type except Beggars.
The function `prepare_citizens_menu_ui` at `0x0040B570` calculates the satisfaction classes by converting the `i16` into an `f32`, and picking the highest applicable class:

|Satisfaction >|Satisfaction Class|
|-|-|
|29,5|Very Happy|
|19,5|Happy|
|9,5|Very Satisfied|
|0,5|Satisfied|
|-10,5|Dissatisfied|
|-Infinity|Annoyed|


The function `update_citizen_satisfaction` at `0x0051C830` calculates the satisfaction each population type would have, and then increases or decreases the value by the *step size*.
At `0x006736AC` there is a table that contains for every difficulty the step sizes for increments and decrements to the satisfaction:

|Needs|Increment|Decrement|
|-|-|-|
|Low|3|1|
|Normal|2|1|
|High|1|2|
|Unused|1|1|

At `0x006736A0` there is a table that contains for every difficulty the *base satisfaction* for every population type:

|Needs|Rich|Wealthy|Poor|
|-|-|-|-|
|Low|249|244|236|
|Normal|243|238|229|
|High|236|231|224|




