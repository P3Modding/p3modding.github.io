# Tavern Interaction

The tavern interaction operations are enqueued by the tavern's panel when switching between the tavern's pages.
The following fields have been identified:

```c
struct operation_tavern_interaction
{
  int field_0_rand;
  int field_4_merchant_index;
  int field_8_town_index;
  tavern_interaction field_C_interaction_type;
};
```

Depending on the interaction type, one of the following actions may be done.

## 1

## 3 and 8

## 5

## Weapons Dealer
If the interaction's merchant index is invalid, the town's weapons dealer is unlocked, and no other action is performed.
This happens if a merchant navigates from the weapons dealer page to a different page.

Otherwise if the town's weapons dealder is unlocked, it'll be locked to the merchant, and a criminal investigation might be started.
An investigation is started only if all of the following conditions are met:
- The merchant is not the alderman
- The merchant is not the mayor in the particular town
- The town is not sieged, blocked, boycotted or under pirate attack
- The following formula is true: `(rand & 0x3ff) < 102`
- The following formula is true: `weaponsdealer_timestamp < now + 0x200`

If all conditions are met, the investigation scheduled task is scheduled at `(now + 0x200) | 0x80`, and the weapons dealer timestamp is set to `now`.

## Burglar
The burglar is handled like the weapons dealer, except the exceptions for alderman, local mayor and town status don't exist.

## 9

## Leave
