# Beggar Satisfaction Bug

## Summary
The satisfaction of beggars never decreases, but increases if a town wins a siege.

## Details
The `update_citizen_satisfaction` function at `0x0051C830` calculates the satisfaction for all population types except beggars, so the beggar satisfaction should not change throughout the game.

However, the `tick_siege` function at `0x00629A50` gives every population type *including beggars* a bonus of 20 satisfaction when the town repels the attackers, bypassing the satisfaction step size.

Since the beggar satisfaction is influencing the beggar immigration, this bug has a gameplay impact: The more sieges a town wins, the more beggars it will attract.

## Fix
The following code distributes the satisfaction bonus, where `edx` contains the (decrementing) loop variable, `ecx` the current population type and `eax` the (u16) offset in the towns array.
```asm
.text:00629A32                 mov     edx, 4
.text:00629A37
.text:00629A37 loc_629A37:                             ; CODE XREF: tick_siege+1872↓j
.text:00629A37                 xor     eax, eax
.text:00629A39                 mov     al, [esi+5D3h]
.text:00629A3F                 lea     ebx, [eax+eax*4]
.text:00629A42                 shl     ebx, 6
.text:00629A45                 sub     ebx, eax
.text:00629A47                 lea     eax, [ecx+ebx*4]
.text:00629A4A                 mov     ebx, static_game_world.field_68_towns
.text:00629A50                 add     word ptr [ebx+eax*2+300h], 14h
.text:00629A59                 lea     eax, [ebx+eax*2+300h]
.text:00629A60                 inc     ecx
.text:00629A61                 dec     edx
.text:00629A62                 jnz     short loc_629A37
.text:00629A64                 mov     al, [esi+61Ch]
.text:00629A6A                 test    al, al
.text:00629A6C                 jz      short loc_629A8E
.text:00629A6E                 xor     eax, eax
.text:00629A70                 push    edi
.text:00629A71                 mov     al, [esi+5D3h]
.text:00629A77                 mov     ecx, eax
.text:00629A79                 shl     ecx, 7
.text:00629A7C                 add     ecx, eax
.text:00629A7E                 lea     edx, [eax+ecx*8]
.text:00629A81                 mov     eax, static_class26_ptr
.text:00629A86                 lea     ecx, [eax+edx*4]
.text:00629A89                 call    sub_634C50
```
Since the loop body does not interact with `edx`, it is sufficient to initialize `edx` to `3` instead of `4`.
To archive that, the operation `BA 04 00 00 00` needs to be replaced with `BA 03 00 00 00`.