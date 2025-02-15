# Trade Routes (.rou)
The saved trade routes are stored in `./Save/AutoRoute`.
An uncomporessed trade route is an array of route stops, 220 bytes each.
The rou file format is defined as:
```
          | 00  01   02  03   04  05   06  07 |
00000000  | Output Length   | Data            |
```

If the output length is bigger than `0` the file is compressed.
Otherwise the absolute value of the negative output length denotes the length.

## Compression
The compression algorithm has not been identified, but the decompression was [reproduced](https://github.com/P3Modding/p3-lib/tree/master/p3-rou).

## Trade Route Stops
A trade route stop is defined as:
```
          |           00           01           02           03           |
00000000  | Unused                        | Town Index | Action           |
00000004  | Ware Order Array                                              |
...
0000001c  | Ware Price Array                                              |
...
0000007c  | Ware Amount Array                                             |
```
The "direction" of a transaction is encoded in the price and amount:

|Price|Amount|Direction|
||||
|0|Negative|Ship -> Office|
|0|Positive|Office -> Ship|
|Positive|Positive|Ship -> Town|
|Negative|Positive|Town -> Ship|

The "Max" amount is represented by `1_000_000_000` for both barrel and bundle wares.
