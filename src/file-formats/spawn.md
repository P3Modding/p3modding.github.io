# Spawn Points (.spawn)
Spawn data of a town is stored in `./iso/towns/<id>.spawn`
(`SpawnFormat=spawn` in `iso.ini`).

The file is an array of `uint32` values that decode as pairs and appear to be
grouped into sections, similar to the [nodes](./nodes.md) file:
```
          | 00  01   02  03   04  05   06  07 |
00000000  | A      | B      | A      | B      |
```
The first value of each pair (`A`) lies in the tile-column range (`0..127`),
while the paired value (`B`) increases monotonically within a run. The exact
field semantics and section boundaries have not been identified.
