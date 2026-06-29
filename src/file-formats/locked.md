# Build Mask (.locked)
The build mask of a town is stored in `./iso/towns/<id>.locked`
(`LockFormat=locked` in `iso.ini`).

It is a flat array of one byte per tile covering the town area only
(`128 x 226 = 28928` bytes, no header).

| Value | Meaning |
|-|-|
| `0x00` | buildable |
| `0x01` | locked |

The entry for column `x` and row `y` (`0..225`) is the byte at `y * 128 + x`.
The covered area matches rows `0..225` of the [town map](./town.md).
