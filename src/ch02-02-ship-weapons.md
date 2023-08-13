# Ship Weapons

Ship Weapons are represented by the following enum:
```rust
pub enum ShipWeaponId {
    SmallCatapult = 0x00,
    SmallBallista = 0x01,
    LargeCatapult = 0x02,
    LargeBallista = 0x03,
    Bombard = 0x04,
    Cannon = 0x05,
}
```
Cutlasses are not ship weapons.

## Ship Weapon Scaling
The amounts P3 displays in-agem are not the values the game uses under the hood.

A table that maps every `ShipWeaponId` to its scaling factor can be found at `0x00672CB4`.
This reveals the following factors:
```rust
ShipWeaponId::SmallCatapult => 1000
ShipWeaponId::SmallBallista => 1000
ShipWeaponId::LargeCatapult => 2000
ShipWeaponId::LargeBallista => 2000
ShipWeaponId::Bombard => 2000
ShipWeaponId::Cannon => 1000
```
