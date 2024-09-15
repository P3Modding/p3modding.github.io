# Projectiles

## Ship Artillery Projectiles
The `sea_battle_local_map_ship_fire_volley` function at `0x0061E8EF` loops over the artillery slots of the selected side.
It restricts the target coordinates to be in the cone of fire, and calls `sea_battle_local_map_ship_fire_shot` at `0x006214CB` for every artillery piece.
