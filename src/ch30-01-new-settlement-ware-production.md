# New Settlement Ware Production Bug

## Summary
Do to an [off-by-one error](https://en.wikipedia.org/wiki/Off-by-one_error), a town founded through the alderman mission does not produce the goods the Hanse needs most, but instead those of the adjacent facility id.

## Details
The `determine_new_settlement` function at `0x00532E30` calculates the wares with the biggest need.
Then it attempts to build a bitmap in which a `1` denotes that the nth production facility should be effective.
This is pseudeocode of the bit position calculation:

```c
(1 << (ware_to_facility_mapping[ware_id] - 3)) & 0xFFFFFF;
```

Production facilities start at id `0x04` (hunting lodge), but P3 subtracts only `3` from the facility id.
Therefore, if the Hanse has a shortage of skins, the bitmap will have `0b0000000000000010` set instead of `0b0000000000000001`.
The second production facility is fisherman's hut (`0x05`), so a shortage of skins causes an effective fish production, and so forth.

## Fix
Subtracting `4` instead of `3` fixes this bug.
The subtraction is at `0x00532FF1`:
```asm
.text:00532FE2 loc_532FE2:                             ; CODE XREF: determine_new_settlement+1EA↓j
.text:00532FE2                 mov     edx, [esp+edi*4+0F0h+effective_ware_ids]
.text:00532FE6                 mov     eax, 1
.text:00532FEB                 mov     cl, ds:ware_to_prod_mapping[edx]
.text:00532FF1                 sub     ecx, 3
.text:00532FF4                 shl     eax, cl
.text:00532FF6                 mov     ecx, [esi]
.text:00532FF8                 and     eax, 0FFFFFFh
.text:00532FFD                 test    eax, ecx
.text:00532FFF                 jnz     short loc_533007
.text:00533001                 or      ecx, eax
.text:00533003                 mov     [esi], ecx
.text:00533005                 jmp     short loc_53300C
```
To change the `3` to a `4`, the operation `83 E9 03` needs to be replaced with `83 E9 04`.
