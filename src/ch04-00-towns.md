# Towns

P3 has 40 different towns, which are assigned to one of 5 different regions:

|Id|Name|
|-|-|
|0|West|
|1|North|
|2|North Sea Area|
|3|Baltic Sea Area|
|4|East|

Towns are indentified by their id, and `scripts/StadtDaten.ini` defines details such as the corresponding region:

|Id|Name|Region|
|-|-|-|
|0|Edinburgh|West|
|1|Newcastle|West|
|2|Scarborough|West|
|3|Boston|West|
|4|London|West|
|5|Bruges|West|
|6|Haarlem|North Sea Area|
|7|Harlingen|North Sea Area|
|8|Groningen|North Sea Area|
|9|Cologne|North Sea Area|
|10|Bremen|North Sea Area|
|11|Ripen|North Sea Area|
|12|Hamburg|North Sea Area|
|13|Flensburg|North Sea Area|
|14|Luebeck|North Sea Area|
|15|Rostock|North Sea Area|
|16|Bergen|North|
|17|Stavanger|North|
|18|Toensberg|North|
|19|Oslo|North|
|20|Aalborg|North|
|21|Goeteborg|North|
|22|Naestved|North|
|23|Malmoe|North|
|24|Ahus|North|
|25|Stockholm|North|
|26|Visby|North|
|27|Helsinki|North|
|28|Stettin|Baltic Sea Area|
|29|Ruegenwald|Baltic Sea Area|
|30|Gdansk|Baltic Sea Area|
|31|Torun|Baltic Sea Area|
|32|Koenigsberg|Baltic Sea Area|
|33|Memel|Baltic Sea Area|
|34|Windau|East|
|35|Riga|East|
|36|Pernau|East|
|37|Reval|East|
|38|Ladoga|East|
|39|Novgorod|East|

The "Found Settlement" alderman mission UI does not use the definitions from `scripts/StadtDaten.ini`, but instead uses the following hardcoded mapping:

|Id|Name|Region|
|-|-|-|
|0|Edinburgh|West|
|1|Newcastle|West|
|2|Scarborough|West|
|3|Boston|West|
|4|London|West|
|5|Bruges|West|
|6|Haarlem|North Sea Area|
|7|Harlingen|North Sea Area|
|8|Groningen|North Sea Area|
|9|Cologne|North Sea Area|
|10|Bremen|North Sea Area|
|11|Ripen|North Sea Area|
|12|Hamburg|North Sea Area|
|13|Flensburg|Baltic Sea Area|
|14|Luebeck|Baltic Sea Area|
|15|Rostock|Baltic Sea Area|
|16|Bergen|North|
|17|Stavanger|North|
|18|Toensberg|North|
|19|Oslo|North|
|20|Aalborg|North|
|21|Goeteborg|North|
|22|Naestved|North|
|23|Malmoe|North|
|24|Ahus|North|
|25|Stockholm|North|
|26|Visby|North|
|27|Helsinki|North|
|28|Stettin|Baltic Sea Area|
|29|Ruegenwald|Baltic Sea Area|
|30|Gdansk|Baltic Sea Area|
|31|Torun|Baltic Sea Area|
|32|Koenigsberg|Baltic Sea Area|
|33|Memel|East|
|34|Windau|East|
|35|Riga|East|
|36|Pernau|East|
|37|Reval|East|
|38|Ladoga|East|
|39|Novgorod|East|

## Town Struct
The pointer to the towns array is stored in the static `game_world` struct at offset `0x68`, and the size of that array at offset `0x10`.
**A town's id is not its index in the towns array**.

The following fields have been identified:
```
00000000 town struc ; (sizeof=0x9F8, mappedto_112)
00000000                                         ; XREF: town_wrapper/r
00000000 field_0_storage storage ?
000002C0 field_2C0_town_index db ?
000002C1 field_2C1_raw_town_id db ?
000002C2 field_2C2 db ?
000002C3 field_2C3_famine_counter db ?
000002C4 field_2C4 dw ?
000002C6 field_2C6_land_tax dw ?
000002C8 field_2C8_town_flags dd ?
000002CC field_2CC dd ?
000002D0 field_2D0_celebration_timestamp dd ?
000002D4 field_2D4_total_citizens dd ?
000002D8 field_2D8_citizens dd 4 dup(?)
000002E8 field_2E8_citizens_old dd 4 dup(?)
000002F8 field_2F8_citizens_dwellings_occupied dw 3 dup(?)
000002FE db ? ; undefined
000002FF db ? ; undefined
00000300 field_300_citizens_satisfaction dw 4 dup(?)
00000308 field_308 dw 4 dup(?)
00000310 field_310_daily_consumptions_citizens dd 24 dup(?)
00000370 field_370 dd ?
00000374 field_374 dd ?
00000378 field_378 dd ?
0000037C field_37C dd ?
00000380 field_380 dd ?
00000384 field_384 dd ?
00000388 field_388 dd ?
0000038C field_38C dd ?
00000390 field_390 dd ?
00000394 field_394 dd ?
00000398 field_398 dd ?
0000039C field_39C dd ?
000003A0 field_3A0 dd ?
000003A4 field_3A4 dd ?
000003A8 field_3A8 dd ?
000003AC field_3AC dd ?
000003B0 field_3B0 dd ?
000003B4 field_3B4 dd ?
000003B8 field_3B8 dd ?
000003BC field_3BC dd ?
000003C0 field_3C0 dd ?
000003C4 field_3C4 dd ?
000003C8 field_3C8 dd ?
000003CC field_3CC dd ?
000003D0 field_3D0_wares_copy dd 24 dup(?)
00000430 field_430_unknown_wares_data dd 24 dup(?)
00000490 field_490_weird_prods dd 24 dup(?)
000004F0 field_4F0_consumption_data consumption_data 24 dup(?)
00000670 field_670 dd ?
00000674 field_674 dd ?
00000678 field_678 dd ?
0000067C field_67C dd ?
00000680 field_680 dd ?
00000684 field_684 dd ?
00000688 field_688 dd ?
0000068C field_68C dd ?
00000690 field_690 dd ?
00000694 field_694 dd ?
00000698 field_698 dd ?
0000069C field_69C dd ?
000006A0 field_6A0 dd ?
000006A4 field_6A4 dd ?
000006A8 field_6A8 dd ?
000006AC field_6AC dd ?
000006B0 field_6B0 dd ?
000006B4 field_6B4 dd ?
000006B8 field_6B8 dd ?
000006BC field_6BC dd ?
000006C0 field_6C0 dd ?
000006C4 field_6C4 dd ?
000006C8 field_6C8 dd ?
000006CC field_6CC dd ?
000006D0 field_6D0 dd ?
000006D4 field_6D4 dd ?
000006D8 field_6D8 dd ?
000006DC field_6DC dd ?
000006E0 field_6E0 dd ?
000006E4 field_6E4 dd ?
000006E8 field_6E8 dd ?
000006EC field_6EC dd ?
000006F0 field_6F0 db ?
000006F1 field_6F1_mayor_id db ?
000006F2 field_6F2 db ?
000006F3 field_6F3 db ?
000006F4 field_6F4_recent_extra_taxes_amount dd ?
000006F8 field_6F8_head_tax_rate_and_extra_tax_timestamp dd ?
000006FC field_6FC dd ?
00000700 field_700_money dd ?
00000704 field_704_transactions dd 11 dup(?)
00000730 field_730 dd ?
00000734 field_734 dd ?
00000738 field_738 dd ?
0000073C field_73C dd ?
00000740 field_740 dd ?
00000744 field_744 dd ?
00000748 field_748 dd ?
0000074C field_74C dd ?
00000750 field_750 dd ?
00000754 field_754 dd ?
00000758 field_758 dd ?
0000075C field_75C dd ?
00000760 field_760 dd ?
00000764 field_764 dd ?
00000768 field_768 dd ?
0000076C field_76C_more_flags dd ?
00000770 field_770 db ?
00000771 field_771 db ?
00000772 field_772 db ?
00000773 field_773 db ?
00000774 field_774 dw ?
00000776 field_776 dw ?
00000778 field_778 dd ?
0000077C field_77C dd ?
00000780 field_780 dd ?
00000784 field_784_office_index dw ?
00000786 field_786 dw ?
00000788 field_788 db ?
00000789 field_789_wells db ?
0000078A field_78A db ?
0000078B field_78B db ?
0000078C field_78C dw ?
0000078E field_78E dw ?
00000790 field_790_streets_built dw ?
00000792 field_792_streets_total dw ?
00000794 field_794_church church ?
000007A4 field_7A4_town_class1 town_class1 ?
00000810 field_810 dd ?
00000814 field_814 dd ?
00000818 field_818 dd ?
0000081C field_81C dd ?
00000820 field_820 dd ?
00000824 field_824_current_ship_level db 4 dup(?)
00000828 field_828_always_zero db 4 dup(?)
0000082C field_82C dd ?
00000830 field_830 dd ?
00000834 field_834 db ?
00000835 field_835 db ?
00000836 field_836 db ?
00000837 field_837 db ?
00000838 field_838 dd ?
0000083C field_83C db ?
0000083D field_83D db ?
0000083E field_83E db ?
0000083F field_83F db ?
00000840 field_840_class12_array class12 20 dup(?)
00000980 field_980 dd ?
00000984 field_984 dd ?
00000988 field_988 dd ?
0000098C field_98C dd ?
00000990 field_990_outrigger_value dd ?
00000994 field_994_outrigger_id dw ?
00000996 field_996 dw ?
00000998 field_998 db ?
00000999 field_999 db ?
0000099A field_99A db ?
0000099B field_99B db ?
0000099C field_99C dd ?
000009A0 field_9A0 dd ?
000009A4 field_9A4 dd ?
000009A8 field_9A8 dd ?
000009AC field_9AC dd ?
000009B0 field_9B0 dd ?
000009B4 field_9B4 dd ?
000009B8 field_9B8 dd ?
000009BC field_9BC dd ?
000009C0 field_9C0 dd ?
000009C4 field_9C4 dd ?
000009C8 field_9C8 dd ?
000009CC field_9CC dd ?
000009D0 field_9D0 dd ?
000009D4 field_9D4 dd ?
000009D8 field_9D8 dd ?
000009DC field_9DC dd ?
000009E0 field_9E0 dd ?
000009E4 field_9E4 dd ?
000009E8 field_9E8 dd ?
000009EC field_9EC dd ?
000009F0 field_9F0 dd ?
000009F4 field_9F4 dd ?
000009F8 town ends
```