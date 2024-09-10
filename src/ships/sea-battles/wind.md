# Wind

The wind's angle is stored in an `u8` at offset `0x670`.

|Value|Direction|
|-|-|
|0x00|North|
|0x40|East|
|0x80|South|
|0xc0|West|

The `update_sea_battle_wind_direction` function at `0x006113c9` changes the direction by adding or subtracting `8` from the current value, and thus changing the wind direction by `11.25°`.
