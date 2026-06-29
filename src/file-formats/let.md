# Isometric Tiles (.let)
Individual isometric tiles are stored in `./iso/let/<name>.let`
(`TileFormat=let` in `iso.ini`). A `.let` file is a small (~104 byte) descriptor
that binds a tile to its bitmap; it does not contain pixel data itself.

The descriptor is defined as:

| Offset | Type | Field |
|-|-|-|
| `0x08` | `u8[4]` | colour key, magenta `FF 00 FF` |
| `0x10` | `uint32` | tile width (`34`) |
| `0x14` | `uint32` | tile height (`21`) |
| `0x30` | `uint32` | source width |
| `0x34` | `uint32` | source height |
| `0x38` | `uint32` | path length |
| `0x3c` | ASCII | NUL-terminated path to the [`.aim`](./aim.md) bitmap |

For example, `1_1.let`:
```
0000  00 52 1b 01 0e 00 00 00 ff 00 ff ff 00 00 00 00
0010  00 00 00 00 22 00 00 00 15 00 00 00 01 00 00 00
0020  01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0030  22 00 00 00 15 00 00 00 28 00 00 00 69 6d 61 67   "imag
0040  65 73 5c 6d 6f 64 75 6c 65 5f 73 74 61 64 74 6b   es\module_stadtk
0050  61 72 74 65 2f 77 61 73 73 65 72 5f 6e 65 75 2e   arte/wasser_neu.
0060  61 69 6d 00 00 00 00 00                           aim
```
points at `images\module_stadtkarte/wasser_neu.aim` (water).

The tile size (`34 x 21`) matches `TileSize` in `iso.ini`. Tiles named
`1_1`..`9_9` are ground tilesets; the remaining named files are objects.
Variants are bundled by [tile groups](./lgr.md).
