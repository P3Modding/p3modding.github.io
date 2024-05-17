# Time
The game time is stored in the static `game_world` struct at offset `0x14` as *ticks*, and is increased by the `advance_time` function at `0x00530E80`.

## Ticks
Every ingame day is 256 ticks long, so there are 93440 ticks in a year.
Consequently the least significant byte conveniently encodes the time of day.

## Ticking Objects
Different game objects tick at different intervals.
Information about what happens in those ticks can be found in the respective chapters.

### Towns
Towns tick if one of the following equations is true:
```c
game_time & 0b111 == 0b011 &&
town_index == (((unsigned __int8)game_time) + 255) >> 3
```
```c
game_time & 0b111 == 0b111 &&
town_index == ((unsigned __int8)game_time) >> 3
```
This results in the following town tick behaviour:

|Town Index|Game Time LSB|
|-|-|
|32|0b00000_011|
|33|0b00001_011|
|34|0b00010_011|
|35|0b00011_011|
|...|...|
|39|0b00111_011|
|00|0b00000_111|
|01|0b00001_111|
|02|0b00010_111|
|03|0b00011_111|
|...|...|
|31|0b11111_111|

#### Facilities
All facilities tick when their town ticks.
