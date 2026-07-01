# Town Map (.town)
The isometric tile map of a town is stored in `./iso/towns/<id>.town`.
A sibling file `<id>.editor` uses the same layout.

Every shipped `.town` is **231450 bytes**. It is **two stacked tile layers on one
`128 x 226` grid** — a *ground* layer and an *object* layer — not a single tall
grid. Rendering the object layer **on top of** the ground layer (same `x,y`)
reproduces the town; laying the two halves out one below the other makes the map
look duplicated.

## Layout

```
0x00000  Header     10 bytes
0x0000A  Layer 0    GROUND  : 128*226 cells * 4 bytes = 115712 bytes
0x1C40A  Layer 1    OBJECTS : 128*226 cells * 4 bytes = 115712 bytes
0x3880A  Footer     16 bytes
```

| Section | Offset | Size | Contents |
|-|-|-|-|
| Header  | `0x0000` | `10` | see below |
| Ground layer | `0x000A` | `128*226*4 = 115712` | terrain, always fully filled |
| Object layer | `0x1C40A` | `115712` | trees / decorations / structures, sparse |
| Footer  | `0x3880A` | `16` | not yet identified (varies per town) |

`10 + 2 * (128 * 226 * 4) + 16 = 231450`.

## Header (10 bytes)

| Offset | Type | Field | Value |
|-|-|-|-|
| `0x00` | `uint16` | magic | `256` |
| `0x02` | `uint16` | **width** | `128` |
| `0x04` | `uint16` | _pad_ | `0` |
| `0x06` | `uint16` | **height** | `226` |
| `0x08` | `uint16` | _pad_ | `0` |

The first 10 bytes are identical across all towns; byte `0x0A` onward is per-town
map data.

## Cell (4 bytes)

Each cell of each layer is:

```
          | 00  01  | 02  03 |
00000000  | Tile ID |  Aux   |
```

- **Tile ID** — `uint16`, the [`.let`](./let.md) `TextureID` to draw (`0` = empty).
  Every `.let` carries its id as a `u16` at offset `0x02`, so scanning `iso/let/`
  gives the full `Tile ID → tile/image` table (923 tiles, ids `1..923`).
- **Aux** — `uint16` packing elevation and a slope code as `Aux = (Level << 8) | Slope`:

| Slope | Meaning |
|-|-|
| `0x00` | flat |
| `0x01`..`0x06` | slope direction |
| `0xff` | scarp / cliff edge |

The cell `(x, y)` — column `x` in `0..127`, row `y` in `0..225` — of layer `L`
(`0` = ground, `1` = objects) is at:

```
0x0A + (L * 128 * 226 + y * 128 + x) * 4      // Tile ID at +0, Aux at +2
```

## The two layers

- **Ground (layer 0)** is 100% filled: grass, sand, water, cliffs, mountains,
  dirt paths, piers/quay walls. Water ids cluster high (`≈226+`), land low.
- **Object (layer 1)** is sparse (~8% of cells): trees, bushes, fences, barrels,
  monuments and a handful of fixed structures placed on top of the ground.
  The player's economic buildings (houses, church, market, warehouses, …) are
  placed by the game at runtime and are **not** stored here.

A renderer draws in **two passes**: first the whole **ground** layer back-to-front
by the isometric diagonal `x + y`, then the whole **object** layer the same way.
Terrain never occludes objects — a building on a back cell must not be hidden by
water/ground tiles on front diagonals.

**Multi-cell buildings fill a footprint but draw once.** A 2-D building (a `.let`
with `cols > 1` *and* `rows > 1`, e.g. `lager1` at `2x2`) writes the **same
`Tile ID` into every cell of its footprint** (a connected group of equal ids),
but the sprite is blitted **once**, at the footprint's **front cell**
(largest `x + y`); the other cells act as an occupancy/collision mask. Blitting
at every footprint cell draws the building several times over. Cliffs/mountains
(on the *ground* layer) and `1xN` trees are instead placed **per cell** and simply
overhang their neighbours.

**The `Aux` word of a building's cells is not zero.** Each footprint cell carries
a per-cell code in its object-layer `Aux` (the footprint's origin cell has low
byte `0xFF`; the other cells carry small codes `0x00/0x01/0x02…`, and the high
byte tracks a slice/elevation value). It encodes the footprint's shape and
orientation — a `2x2` `lager1` has, e.g., `0x01FF / 0x0000 / 0x0201 / 0x0002`
across its four cells. Placing a building by writing only the `Tile ID` (with
`Aux = 0`) makes the game render it incorrectly; a correct placement must
reproduce the whole footprint's `Aux` values (easiest to copy from a real one).

## Cell projection

Each cell is drawn as an isometric diamond of `34 x 21` px (`TileSize=34 21 0` in
`iso.ini`). Screen position of `(x, y)` uses `DownVector=17 11 0`:

```
screen_x = (x - y) * 17
screen_y = (x + y) * 11
```

Sprites are **bottom-anchored**: the `34 x 21` base diamond lands on the cell, so
tall sprites (piers, trees, walls, buildings) rise upward and legitimately overhang
neighbouring cells rather than fitting inside a single diamond. The `Cols x Rows`
span in the [`.let`](./let.md) is the sprite's tile size; a 2-D building is drawn
once at its footprint's front cell (see above), everything else per cell.

## Related town files

The same `<id>` has companion files: [`.locked`](./locked.md) (build mask),
[`.nodes`](./nodes.md), `.spawn`, and the rendered [`.aim`](./aim.md) minimap.
