# Increase Alderman "Found Settlement" Mission Limit

## Summary
This patch allows the player build towns beyond the 26th town through the "Found Settlement" mission.

## Details
The `schedule_prep_alderman_missions` function at `0x005326E0` schedules a prepare mission operation for every eligible alderman mission type.
The new settlement mission is eligible if the total amount of towns is below 26.

## Patch
The comparion is at `0x0053275C`:
```
.text:0053275C                 cmp     dword ptr [ebp+10h], 1Ah
```

To replace the limit of 26, the `1A` in the operation `83 7D 10 1A` has to be replaced with a different immediate value.
