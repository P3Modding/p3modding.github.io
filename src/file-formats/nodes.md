# City Nodes (.nodes)
The polyline data of a town is stored in `./iso/towns/<id>.nodes`
(`NodesFormat=nodes` in `iso.ini`).

It is a list of sections, each holding a number of nodes (polylines), each
holding a number of points. All values are `uint32`. The file format is defined
as:
```
File    := Section[]
Section := { SectionID, NodeCount, Node[NodeCount] }
Node    := { PointCount, Point[PointCount] }
Point   := { X, Y }
```
A sample file holds 5 sections (60 nodes, 303 points):

| Section | Nodes | Description |
|-|-|-|
| 0 | 24 | ships town docking path (polylines starting near `y = 10`) |
| 1, 2 | 3 + 3 | citizen route paths (those boundaries have to be 22pixel apart) |
| 3 | 1 | small 4 point region |
| 4 | 29 | detail features |

The coordinates use a pixel/unit space (observed `X` `17..4352`, `Y`
`10..2353`), not the tile grid.
