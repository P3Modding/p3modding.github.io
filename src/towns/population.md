# Population
All things related to the population are handled during the town's tick call.
The following subsections explain the identified functions.

The game uses the following enum to represent the 4 population types:
```c
enum population_type : __int32
{
  pt_rich = 0x0,
  pt_wealthy = 0x1,
  pt_poor = 0x2,
  pt_beggar = 0x3,
};
```
