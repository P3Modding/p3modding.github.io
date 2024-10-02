# Initialization
Sieges are started by operation type `0x8E`, the `handle_start_siege` function is at `0x00633AF0`.

## Army Size
|Siege Type|Swords|Bows|Crossbows|Carbines|Trebuchets|
|-|-|-|-|-|-|
|0|262|131|99|0|55|
|2|262|131|0|87|55|
|3|262|0|99|87|55|

The attacking squads are then enforced to be below or equal to the following values defined at `0x0067B604`:

|Squad|Limit|
|-|-|
|Swords|40|
|Bows|22|
|Crossbows|18|
|Carbines|15|
|Trebuchets|6|

## Gate and Ram
Both the gate and the battering ram have 0x10000 (65536) HP.

## Approach

