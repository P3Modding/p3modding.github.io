# Buildings
New building ids, used in operations that create new buildings, are represented by the following enum:
```rust
pub enum NewBuildingId {
    Well = 0x28,
    Tower = 0x29, // Cannon, Bombard; Gate, Port
    HousePoor = 0x2a,
    PitchShoot = 0x2f,
    HouseWealthy = 0x50,
    HouseRich = 0x51,
    FarmGrain = 0x53,
    FarmHemp = 0x54,
    FarmSheep = 0x55,
    FarmCattle = 0x56,
    FishermansHouse = 0x57,
    Brewery = 0x58,
    Apiary = 0x59,
    WeavingMill = 0x5a,
    Workshop = 0x5b,
    Vineyard = 0x5c,
    HuntingLodge = 0x5d,
    Saltworks = 0x5e,
    IronSmelter = 0x60,
    Pitchmaker = 0x61,
    Brickworks = 0x62,
    Pottery = 0x63,
    Sawmill = 0x64,
    Hospital = 0x65,
    Warehouse = 0x66,
    Mint = 0x67,
    School = 0x68,
    Chapel = 0x69,
}
```

At `0x672fbf` is a table that maps building ids to new building ids:

|BuildingId|NewBuildingId|
|-|-|
|0x00|0x2c|
|0x01|0x1b|
|0x02|0x0b|
|0x03|0x08|
|0x04|HuntingLodge|
|0x05|FishermansHouse|
|0x06|Brewery|
|0x07|Workshop|
|0x08|Apiary|
|0x09|FarmGrain|
|0x0a|FarmCattle|
|0x0b|Sawmill|
|0x0c|WeavingMill|
|0x0d|Saltworks|
|0x0e|IronSmelter|
|0x0f|FarmSheep|
|0x10|Vineyard|
|0x11|Pottery|
|0x12|Brickworks|
|0x13|Pitchmaker|
|0x14|FarmHemp|
|0x15|HouseRich|
|0x16|HouseRich|
|0x17|HouseRich|
|0x18|HouseWealthy|
|0x19|HouseWealthy|
|0x1a|HouseWealthy|
|0x1b|HousePoor|
|0x1c|HousePoor|
|0x1d|HousePoor|
|0x1e|Warehouse|
|0x1f|0x04|
|0x20|0x03|
|0x21|0x0b|
|0x22|0x07|
|0x23|0x00|
|0x24|0x02|
|0x25|0x05|
|0x26|0x09|
|0x27|0x33|
|0x28|0x52|
|0x29|Hospital|
|0x2a|Mint|
|0x2b|School|
|0x2c|Chapel|
|0x2d|0x37|
|0x2e|0x01|
|0x2f|0x5f|
|0x30|Tower|
|0x31|Tower|
|0x32|Tower|
|0x33|Tower|
|0x34|PitchShoot|
|0x35|PitchShoot|