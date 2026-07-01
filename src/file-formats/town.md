# Town Map (.town)
The isometric tile map of a town is stored in `./iso/towns/<id>.town`.
A sibling file `<id>.editor` uses the same layout.

> **What a `.town` does and doesn't hold.** The `.town` is the static *landscape* a town
> is built on: ground (grass/sand), water, cliffs, mountains, vegetation, dirt paths and a
> handful of fixed structures (e.g. quay walls, piers). It does **not** seems to contain the town's
> playable buildings — houses, the church, market, town wall, production facilities, etc. are
> placed by the game's building system at runtime and live in the savegame, not here. 

[To be verified]
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

The `Tile ID` is not a filename, but the lookup **is** stored in the game data: every
[`.let`](./let.md) tile carries its `Tile ID` as a `u16` at offset `0x02`. Scanning
`iso/let/` and reading that field gives the complete `Tile ID → tile/image` table
(923 tiles, ids `1..923`; `0` = empty).

## Tile cell and projection
Each grid cell is drawn as an isometric diamond of `34 x 21` px (`TileSize=34 21 0` in
`iso.ini`) — a dimetric ~1.6:1 shape. Cells are problaby placed half a tile apart using the `DownVector` (17 px across,
~10.5 px down; `iso.ini` rounds it to `17 11`):


## Large objects fill their whole footprint
{To be checked}

A multi-cell object (building, cliff, mountain) is **not** stored in one cell. The same
`Tile ID` is written into **every cell of its `Cols x Rows` footprint** (the footprint is
declared in the [`.let`](./let.md)). For example a `4 x 4` cliff occupies 16 cells that all
hold the same id, and a mountain can fill 180+ cells with one id, tracing the object's
silhouette on the map.

The engine draws the object's sprite **once**, at the footprint **origin** (the back/top
corner — the cell whose west and north neighbours hold a different id), and uses the other
footprint cells purely as an occupancy / picking / collision mask. A renderer must therefore
blit the sprite a single time per object and skip the covered cells; blitting it at every
cell produces heavy overdraw. The sprite is sized for the full `Cols x Rows` area (its width
is `(Cols + Rows) · 17` px), which is why a building's image legitimately "overflows" the one
cell you painted instead of fitting inside a single `34 x 21` diamond.

## Header
The purpose of most of the 26 byte header is not yet identified. The `uint16` at
offset `0x02` holds the map width (`128`).
