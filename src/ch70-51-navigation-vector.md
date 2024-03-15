# Navigation Vector
The vanilla navigation vector is stored in `./navdata/nav_vec.dat`.
The file format is defined as:
```
          | 00  01   02  03 | 04  05 | 06  07 |
00000000  | Length | 00  00 | X      | Y      |
00000008  | X      | Y      | ...             |
```
where `Length` denotes the amount of points, and `X` and `Y` denote the coordinates of each point.

The following sample code converts the navpoint matrix file into a png:
```python
import struct
import imageio
import numpy

WIDTH = 640
HEIGHT = 472
f = open("nav_vec.dat", "rb")
length = struct.unpack("<H", f.read(2))[0]
f.read(2)
print(f"Reading {length} vecs")
image = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)

for i in range(0, length):
    x, y = struct.unpack("<2H", f.read(4))
    image[y, x] = (0xff, 0x00, 0x00)

imageio.imwrite('nav_vec.png', image)
```
![image](nav_vec.png)
