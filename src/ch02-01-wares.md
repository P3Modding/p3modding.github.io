# Ware Types
Wares are represented by the following enum:
```rust
pub enum WareId {
    Grain = 0x00,
    Meat = 0x01,
    Fish = 0x02,
    Beer = 0x03,
    Salt = 0x04,
    Honey = 0x05,
    Spices = 0x06,
    Wine = 0x07,
    Cloth = 0x08,
    Skins = 0x09,
    WhaleOil = 0x0a,
    Timber = 0x0b,
    IronGoods = 0x0c,
    Leather = 0x0d,
    Wool = 0x0e,
    Pitch = 0x0f,
    PigIron = 0x10,
    Hemp = 0x11,
    Pottery = 0x12,
    Bricks = 0x13,
    Sword = 0x14,
    Bow = 0x15,
    Crossbow = 0x16,
    Carbine = 0x17,
}
```
Although the militia weapon are part of the wares enum, the game often uses loops and mapping arrays that exclude them.

## Ware Scaling
The amounts P3 displays in-game are not the values the game uses under the hood.
Every ware has a scaling factor, through which the game divides the actual values.
Wares with a barrel icon have a scaling factor of `200`, Wares with a bundle icon have a scaling factor of `2000`.

A table that maps every barrel `WareId` to `1` and every bundle `WareId` to `0` can be found at `0x00672C14`.
The scaling of militia weapons can be inferred by transferring one piece and observing the value changes in memory.
This reveals the following factors:
```rust
WareId::Grain => 2000
WareId::Meat => 2000
WareId::Fish => 2000
WareId::Beer => 200
WareId::Salt => 200
WareId::Honey => 200
WareId::Spices => 200
WareId::Wine => 200
WareId::Cloth => 200
WareId::Skins => 200
WareId::WhaleOil => 200
WareId::Timber => 2000
WareId::IronGoods => 200
WareId::Leather => 200
WareId::Wool => 2000
WareId::Pitch => 200
WareId::PigIron => 2000
WareId::Hemp => 2000
WareId::Pottery => 200
WareId::Bricks => 2000
WareId::Sword => 10
WareId::Bow => 10
WareId::Crossbow => 10
WareId::Carbine => 10
```
