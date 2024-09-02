# Ships

## Ships Struct
The static ships struct is at `0x006DD7A0`.
The following fields have been identified:
```C
struct __declspec(align(4)) ships
{
  captain *field_0_captains_ptr __tabform(NODUPS);
  ship *field_4_ships;
  convoy *field_8_convoys;
  _DWORD field_C[5];
  class49 field_20_class49_array[16];
  __int16 field_E0;
  unsigned __int16 field_E2_unused_ship_index;
  int field_E4;
  __int16 field_E8_unknown_ship_id;
  __int16 field_EA_ship_index_1;
  signed __int16 field_EC;
  signed __int16 field_EE;
  __int16 field_F0;
  unsigned __int16 field_F2_captains_size;
  unsigned __int16 field_F4_ships_size;
  unsigned __int16 field_F6_convoys_size;
  signed __int16 field_F8;
  signed __int16 field_FA;
  unsigned __int16 field_FC_ship_engagement_range_squared;
  signed __int16 field_FE;
  int field_100;
  int field_104;
};
```

## Ship Struct
The pointer to the ships array is stored in the static `ships` struct at offset `0x04`, and the length of that array at offset `0xf4`.

The following fields have been identified:
```
00000000 struct ship // sizeof=0x180
00000000 {
00000000     unsigned __int8 field_0_merchant_index __tabform(NODUPS);
00000001     char field_1;
00000002     unsigned __int16 field_2;
00000004     unsigned __int16 field_4_next_ship_of_merchant;
00000006     __int16 field_6_next_ship_index_in_convoy;
00000008     unsigned __int16 field_8_convoy_index;
0000000A     unsigned __int16 field_A_some_ship_id;
0000000C     unsigned __int16 field_C_next_spotted_candidate;
0000000E     unsigned __int8 field_E_ship_type;
0000000F     unsigned __int8 field_F_maybe_upgrade_level;
00000010     int field_10_capacity;
00000014     int field_14_max_health;
00000018     int field_18_current_health;
0000001C     int field_1C_x;
00000020     int field_20_y;
00000024     ship_route *field_24_route_ptr;
00000028     int field_28_x_delta;
0000002C     int field_2C_y_delta;
00000030     int field_30;
00000034     signed __int16 field_34;
00000036     char field_36_is_on_route;
00000037     unsigned __int8 field_37_unknown_town_index;
00000038     unsigned __int8 field_38_dest_town_index;
00000039     unsigned __int8 field_39_last_town_index;
0000003A     unsigned __int16 field_3A_target_ship_index;
0000003C     char field_3C;
0000003D     char field_3D;
0000003E     signed __int16 field_3E_maintenance;
00000040     unsigned __int16 field_40;
00000042     unsigned __int16 field_42_captain_index;
00000044     int field_44_timestamp2;
00000048     int field_48_maybe_calculated_arrival_timestamp;
0000004C     int field_4C_timestamp;
00000050     unsigned __int16 field_50_spotted_ships[2];
00000054     unsigned int field_54_wares[24];
000000B4     float field_B4_avg_prices[24];
00000114     int field_114_payload_buy_sum;
00000118     int field_118_maybe_used_capacity;
0000011C     int field_11C_maybe_arty_weight;
00000120     int field_120_arty_stuff;
00000124     int field_124;
00000128     int field_128;
0000012C     int field_12C;
00000130     __int16 field_130;
00000132     unsigned __int16 field_132;
00000134     __int16 field_134_status;
00000136     char field_136;
00000137     char field_137;
00000138     unsigned __int16 field_138_docking_counter;
0000013A     char field_13A;
0000013B     char field_13B;
0000013C     char field_13C_artillery[24];
00000154     int field_154;
00000158     int field_158;
0000015C     char field_15C_is_pirate;
0000015D     unsigned __int8 field_15D;
0000015E     __int16 field_15E;
00000160     char field_160_ship_name[32];
00000180 };
```
