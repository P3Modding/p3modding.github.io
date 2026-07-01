# Isometric Tiles (.let)
Individual isometric tiles are stored in `./iso/let/<name>.let`
(`TileFormat=let` in `iso.ini`). A `.let` is a small (~100–800 byte) descriptor
that binds a tile id to a rectangle inside an [`.aim`](./aim.md) atlas; it holds
no pixel data itself.

## Fixed header (36 bytes)

| Offset | Type | Field | Notes |
|-|-|-|-|
| `0x00` | `u8` | magic0 | always `0x00` |
| `0x01` | `char` | magic1 | always `'R'` (`0x52`) |
| `0x02` | `uint16` | **TextureID** | the id referenced by [`.town`](./town.md) cells |
| `0x04` | `u8` | Type | factory / anim-type selector |
| `0x08` | `uint32` | TransparencyType | `0xFFFF00FF` — magenta `FF 00 FF` colour key |
| `0x0C` | `uint16` | **src_x** | atlas source X (crop left) |
| `0x10` | `uint16` | **src_y** | atlas source Y (crop top) |
| `0x14` | `uint16` | **width** | sprite width in the atlas |
| `0x18` | `uint16` | **height** | sprite height in the atlas |
| `0x1C` | `u8` | cols | horizontal tile span |
| `0x20` | `u8` | rows | vertical tile span |

The fields at `0x0C`–`0x18` are the **atlas source rectangle** — the crop the
renderer takes out of the `.aim` bitmap. For example `klippen_auf2_8.let` stores
`(544, 174, 136, 87)`, i.e. that rectangle inside `KLIPPEN_0.png` (a `1024x1024`
atlas holding a `7x11` grid of `136x87` cliffs). A plain ground tile stores the
whole small bitmap, e.g. `wasser_neu` = `(0, 0, 34, 21)`. All the `uint16` fields
are followed by 2 padding bytes; `cols`/`rows` by 3 padding bytes.

## After the header

```
0x24  ExtHeader   : u32 count, then u32 entries[count]
      FrameTable  : (cols + rows - 1) frames, 16 bytes each: s32 x, y, w, h
      Primary     : u32 length, then "images\module_stadtkarte/NAME.aim" (NUL-terminated)
      u32 variant_count
      Variants    : shadow / snow / scaffolding chunks (type-specific layout)
```

- **Frame table** — the per-animation sub-slices *inside* the source rectangle.
  A `1x1` tile has one frame; a building/cliff has `cols + rows - 1` vertical
  slices. Their bounding box equals the header source rect for 868 of 934 files;
  for the rest the header rect is a few transparent rows taller at the top (same
  bottom edge). Cropping the **header rect** is the reliable choice.
- **Primary** — the length-prefixed path to the `.aim` atlas actually rendered.
  The converted PNG is `<NAME>_0.png` (the whole atlas canvas); the header rect
  selects the sub-image.
- **Variants** — additional length-prefixed `.aim` paths for the shadow,
  seasonal snow and under-construction (`BGeruest`) versions. Each variant chunk
  has a type-specific layout and still ends in a `Primary`-style path.

## Example — `1_1.let` (water, a `1x1` ground tile)

```
0000  00 52 1b 01 0e 00 00 00  ff 00 ff ff 00 00 00 00
      |  R  TexID Ty  pad      TranspType   src_x src_y
0010  00 00 00 00 22 00 00 00  15 00 00 00 01 00 00 00
      src_y..    width=34      height=21    cols=1
0020  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
      rows=1     ext_count=0   frame.x=0    frame.y=0
0030  22 00 00 00 15 00 00 00  28 00 00 00 69 6d 61 67   "imag
      frame.w=34 frame.h=21    len=0x28=40  i  m  a  g
0040  65 73 5c 6d 6f 64 75 6c  65 5f 73 74 61 64 74 6b   es\module_stadtk
0050  61 72 74 65 2f 77 61 73  73 65 72 5f 6e 65 75 2e   arte/wasser_neu.
0060  61 69 6d 00 00 00 00 00                            aim
```

`TextureID = 0x011B = 283`, source rect `(0, 0, 34, 21)`, one frame, pointing at
`images\module_stadtkarte/wasser_neu.aim`.

The tile size `34 x 21` matches `TileSize` in `iso.ini`. Tiles named `1_1`..`9_9`
are ground tilesets; the remaining named files are objects. Variants are bundled
by [tile groups](./lgr.md).
