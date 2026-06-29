# Town Map (.town)
The isometric tile map of a town is stored in `./iso/towns/<id>.town`.
A sibling file `<id>.editor` uses the same layout.

A map is a grid of `128 x 452` tiles. The file is a 26 byte header followed by
the tile array of `128 * 452 = 57856` tiles, 4 bytes each (`57856 * 4 = 231424`
bytes), so the tile data begins at offset `0x1a`.

Each tile is defined as:
```
          | 00  01   02  03 |
00000000  | Tile ID | Terrain |
```
`Tile ID` is a `uint16` selecting the ground or object tile (observed range
`0..904`). `Terrain` is a `uint16` that packs the elevation level and a slope
code as `Terrain = (Level << 8) | Slope`:

| Slope | Meaning |
|-|-|
| `0x00` | flat |
| `0x01`..`0x06` | slope direction |
| `0xff` | scarp / cliff edge |

The tile at column `x` (`0..127`) and row `y` (`0..451`) is located at
`0x1a + (y * 128 + x) * 4`.

The grid is split at row `226`: rows `0..225` cover the town itself (the same
area as the [build mask](./locked.md)), while rows `226..451` describe the
surrounding world and sea.

The `Tile ID` does not map directly to a [tile](./let.md) filename. The lookup
from `Tile ID` to a concrete tile is resolved internally by the engine and is
not stored in the game's text files.

## Header
The purpose of most of the 26 byte header is not yet identified. The `uint16` at
offset `0x02` holds the map width (`128`).
