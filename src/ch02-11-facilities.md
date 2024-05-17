# Facilities
Business and miscellaneous buildings are grouped into *facilities*.
```rust
pub enum FacilityId {
    Militia = 0x00,
    Shipyard = 0x01,
    Weaponsmith = 0x03,
    HuntingLodge = 0x04,
    FishermansHut = 0x05,
    Brewery = 0x06,
    Workshop = 0x07,
    Apiary = 0x08,
    FarmGrain = 0x09,
    FarmCattle = 0x0a,
    Sawmill = 0x0b,
    WeavingMill = 0x0c,
    Saltworks = 0x0d,
    IronSmelter = 0x0e,
    FarmSheep = 0x0f,
    Vineyard = 0x10,
    Pottery = 0x11,
    Brickworks = 0x12,
    Pitchmaker = 0x13,
    FarmHemp = 0x14,
}
```
The town's facilities are stored within the town struct.
```
00000000 struct facility // sizeof=0x10
00000000 {                                       // XREF: town/r
00000000     int field_0_efficiency;
00000004     unsigned __int16 field_4_employees;
00000006     unsigned __int8 field_6_type;
00000007     unsigned __int8 field_7_town_index;
00000008     __int16 field_8_productivity;
0000000A     __int16 field_A;
0000000C     __int16 field_C;
0000000E     unsigned __int16 field_E;
00000010 };
```
