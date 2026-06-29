# AIM Images (.aim)
The engine's image format, handled by `AIM.dll` and selected as
`ShaderFormat=aim` in `iso.ini`. It is used both for tile bitmaps in
`./images/module_stadtkarte/` and for baked town overview images in
`./iso/towns/<id>.aim`.

The file starts with the magic `AIM\0`, followed by an embedded name string and
a sequence of chunks of the form `{ Type, Size, Data }`:
```
0000  41 49 4d 00 ...        "AIM\0"
0009  6c 61 6c 61 00         embedded name string
...   chunks { Type, Size, Data }
```

| Chunk Type | Encoding | Example |
|-|-|-|
| `22` | RGB / BGR, uncompressed | town overview `0.aim` (`272 x 155`) |
| `34` | compressed indexed BGRA | tile bitmaps |

Tile bitmaps are sheets of `34 x 21` diamonds keyed on magenta (`FF 00 FF`); a
single file may hold several variants. The overview `iso/towns/<id>.aim` decodes
to a `272 x 155` painted image (the same size as the matching `.tga`), not a tile
render.

`.aim` files can be converted to and from PNG with the community `aim_converter`
tool (`to-png` / `to-aim`).

[To be completed]