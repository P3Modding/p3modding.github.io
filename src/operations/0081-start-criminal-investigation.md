# Start Criminal Investigation
The `handle_operation_81_start_criminal_investigation` at `0x0053FA80` schedules a *Criminal Investigation* task to an indicated timestamp.
The following fields have been identified:
```c
struct operation_81_start_criminal_investigation
{
  signed __int32 field_0_merchant_index;
  signed __int32 field_4_crime_type;
  signed __int32 field_8_delay;
  signed __int32 field_C_town_index;
};
```

The scheduled task's target git difftimestamp is calculated as follows:
```python
(delay + now() + 0x100) & 0x00 | 0x80
```
