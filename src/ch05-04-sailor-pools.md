# Sailor Reputation and Sailor Pools

## Sailor Reputation
A merchant's sailor reputation is stored at `0x1f`.
It influences the growth or decline of the sailor pools.
It ranges from `0` to `20` (inclusive).
During the merchant's tick the sailor reputation is increased by `1`, up to a maximum of `20`.
Dismissing a captain sets the sailor reputation to `0`.


## Sailor Pools
The merchant struct's `sailor_pools` array at offset `0xf0` contains an `u8` for every town (indexed by the town's index), which denotes the size of the sailor pool of the merchant in that town.


