# Criminal Investigation

## Begin
When a criminal investigation task is executed for the first time, the status is `crime_investigation_status_pending`.
The task handler sends a *Charge* or *Indictment* letter to the offending merchant, sets the status to `crime_investigation_status_investigating`, and reschedules the task according to the result of the following computation:
```c
(now + (((now & 7) + 8) << 8)) | 0x80
```

The lower 3 bits of the current time are used as a synchronized pseudorandom number ranging from `0` to `7`.
To that number `8` is added, and the result is shifted by `8` to get a timespan between 8 to 15 days.
That timespan is added to the current time, and the 8th bit is set to constrain the time of day between 12:00 and 24:00.

Both random fields are filled with the result of `rand()` with a `RAND_MAX` of `32767`.

## Verdict
TODO

## Scheduled Task Data
The following task fields have been identified:
```c
struct scheduled_task_criminal_investigation
{
  unsigned __int8 field_0_merchant_index __tabform(NODUPS);
  unsigned __int8 field_1_town_index;
  char field_2;
  unsigned __int8 field_3_hometown_index;
  int field_4_timestamp;
  crime_type field_8_crime_type;
  crime_investigation_status field_9_status;
  unsigned __int16 field_A_random1;
  unsigned __int16 field_C_random2;
  signed __int16 field_E;
};
```

where `crime_type` was found to be:
```c
enum crime_type : unsigned __int8
{
  crime_type_criminal_plans = 0x0,
  crime_type_boycott_broken = 0x1,
  crime_type_pirate_attack = 0x2,
  crime_type_burglary = 0x3,
  crime_type_pirate_sponsor = 0x4,
  crime_type_indecent_behaviour = 0x5,
  crime_type_heresy = 0x6,
  crime_type_round_world = 0x7,
  crime_type_undermining_league = 0x8,
  crime_type_pirate_firing_on_ships = 0x9,
  crime_type_pirate_plundering_ships = 0xA,
  crime_type_pirate_sinking_ships = 0xB,
  crime_type_pirate_capturing_ships = 0xC,
  crime_type_pirate_attacking_town = 0xD,
  crime_type_pirate_firing_on_town = 0xE,
  crime_type_pirate_plundering_town = 0xF,
};
```

and `crime_investigation_status` was found to be:
```c
enum crime_investigation_status : unsigned __int8
{
  crime_investigation_status_pending = 0x0,
  crime_investigation_status_investigating = 0x1,
  crime_investigation_status_confiscation_successful = 0x2,
  crime_investigation_status_unknown = 0x3,
};
```
