# CPR
CPR are archive files used in multiple Ascaron games.
The file format is defined as:
```
          |  00  01  02  03  |  04  05  06  07  |  08  09  0A  0B  |  0C  0D  0E 0F  |
00000000  | Header                                                                   |
00000010  | Version          | Padding                                               |
00000020  | Chunks                                                                   |
```

Each chunk is defined as:
```
00000000  | Index Size       | Unknown          | Files Count      | Data Size       |
00000010  | Index Entries                                                            |
          | Data                                                                     |
```
`Index Size` defines the byte size of the index entries.
`Files Count` defines the amount of entries in the chunk.
`Data Size` defines the size of the data block.

Each index entry is defined as:
```
00000000  | Offset           | Size             | Unknown          | Path            |
00000010  | Path (cont.)                                                             |
```
`Offset` defines the start position relative to the start of the file, and `Size` the size.
`Path` is [latin1 encoded](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) and zero-terminated.

Multiple parsers exist, e.g. [CPRreader](https://gist.github.com/javiercantero/e1042ca2cbb072599c98028c207689fe) and [cprcli](https://github.com/P3Modding/p3-lib/tree/master/cprcli).
