# Tile Groups (.lgr)
Groups of interchangeable tiles are stored in `./iso/let/<name>.lgr`
(`GroupFormat=lgr` in `iso.ini`). Unlike most of the engine's formats, a `.lgr`
file is plain INI text. The engine treats the members as variants of one tile.
```ini
[GROUP]
Type=2
FileCnt=72
File0=0 0 1_6.let
File1=0 0 1_2.let
File2=0 0 1_3.let
...
```
Each `File<n>` entry is `offsetX offsetY <name>.let`, and `FileCnt` is the number
of member [tiles](./let.md). For example, `Wasser_NEU.lgr` groups 72 water tile
variants.
