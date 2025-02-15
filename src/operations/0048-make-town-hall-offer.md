# Make Town Hall Offer
The `handle_operation_48_make_townhall_offer` function at `0x0053B010` handles proposed changes to a town's policy.

```c
struct operation_48_make_town_hall_offer
{
  signed __int32 field_0_meeting_timestamp;
  signed __int32 field_4_extra_tax_amount;
  unsigned __int8 field_8_town_index;
  council_meeting_type field_9_meeting_type;
  signed __int16 field_A_tax_per_head_amount;
  char field_C_merchant_index;
  char field_D;
  char field_E;
  char field_F;
};
```

## Normal Towns
For normal towns a *Council Meeting* scheduled task is scheduled at `0xE00` ticks (14 days) ahead.

## Hanseatic Settlements
Hanseatic settlements have no council and expand military or enlarge town wall offers.
A change to the head tax is applied immediately, and an *Extra Tax* scheduled task is scheduled at the next tick.
