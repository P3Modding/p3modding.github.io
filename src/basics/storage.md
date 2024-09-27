# Storage
The `storage` struct contains a town's or an office's current wares and related data.
Some of the fields have been identified:
```
00000000 ; derived from post-malloc initialization of office and town
00000000 storage         struc ; (sizeof=0x2C0, mappedto_146)
00000000                                         ; XREF: town/r
00000000                                         ; office/r
00000000 field_0         dw ?
00000002 field_2         dw ?
00000004 field_4_current_wares dd 24 dup(?)
00000064 field_64_daily_consumptions_businesses dd 24 dup(?)
000000C4 field_C4_daily_production dd 24 dup(?)
00000124 field_124_ship_weapons dd 6 dup(?)
0000013C field_13C_prod_time_series storage_production_time_series 20 dup(?)
0000027C field_27C       dd ?
00000280 field_280       dd ?
00000284 field_284       dd ?
00000288 field_288       dd ?
0000028C field_28C       dd ?
00000290 field_290       dd ?
00000294 field_294       dd ?
00000298 field_298       dd ?
0000029C field_29C       dd ?
000002A0 field_2A0       dd ?
000002A4 field_2A4       dd ?
000002A8 field_2A8       dd ?
000002AC field_2AC       dd ?
000002B0 field_2B0       dd ?
000002B4 field_2B4       dd ?
000002B8 field_2B8       dd ?
000002BC field_2BC_cutlasses dd ?
000002C0 storage         ends
```