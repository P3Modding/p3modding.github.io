# Unfreeze Port
The `st_unfreeze_port` function at `0x004E94A4`.
It removes the town's `frozen` flag and updates the UI.

```
00000000 struct scheduled_task_unfreeze_port // sizeof=0x4
00000000 {
00000000     signed __int32 field_0_town_index;
00000004 };
```