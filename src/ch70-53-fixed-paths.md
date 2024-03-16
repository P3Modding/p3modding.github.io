# Fixed Paths
Fixed paths are stored in `./navdata/wege_fix.dat`.
The standard game does not appear to load it and does not care if you replace it with arbitrary bytes.
It appears to be a simple length-value encoding:
```
          | 00  01   02  03 | 04  05 | 06  07 |
00000000  | Length          | X      | Y      |
00000008  | ...             | Length          |
...       | X      | Y      | ...
```
The resulting coordinates somewhat resemble the coastlines, but they don't quite fit the navigation matrix.
