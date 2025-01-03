# Bath House Bribes Blunders

## Summary
The bath house bribes are affected by three different bugs:
- If a merchant's offer is lower than the councillor's expectations and the councillor hasn't been bribed by anyone else, the councillor is bribed by the merchant with the index `1`.
- Annoying a councillor in one town affects councillors in all towns.
- Limits on the bribability don't have any effect.

## Details

### Attribution to Merchant `1`
The `handle_operation_bath_house_bribe_failure` function at `0x0053AD10` sets the councillor's briber to `1`, if the councillor was not already bribed by anyone.

This also prevents you from getting the *"Are you there again?! Let me have my bath in peace, please."* line you are supposed to get with annoyed councillors.
Instead you'll get the *"Ah! You're here as well, John Doe? I have only very recently spoken to one of your competitors."* line, since the councillor is now bribed by merchant `1`.

### Unforgiving Bath Houses
The bath house remembers only the index of annoyed local councillors (0-3), and not to which town they belong.
If you annoy the first councillor in one town, the first councillor in every town will stop talking to you, and so forth.

While the annoyed *"Are you there again?! Let me have my bath in peace, please."* line is unreachable in the correct town due to the attribution bug, you do get it if you encounter a councillor with the same index in a different town.

### Limitless Corruption
The `handle_operation_bath_house_bribe_success` function at `0x0053AC50` applies the briber only if a particular value is smaller than 2:
```c
bribed_councillors = 0;
previous_bribing_merchant = static_game_world.field_68_towns[town_index].field_6DC_councillor_bribes[this->args.unknown.arg1];
v6 = 4;
do
{
    if (previous_bribing_merchant == merchant_index)
        ++bribed_councillors;
    --v6;
}
while (v6);
merchant = get_merchant(&static_game_world, merchant_index);
old_recent_donations = merchant->field_4BC_recent_donations;
merchant->field_0_money -= this->args.unknown.arg3;
merchant->field_4BC_recent_donations = this->args.unknown.arg3 + old_recent_donations;
merchant_bribe_success_increase_social_reputation(merchant, this->args.unknown.arg4, this->args.unknown.arg3);
if (bribed_councillors < 2) {
    static_game_world.field_68_towns[this->args.unknown.arg4].field_6DC_councillor_bribes[this->args.unknown.arg1] = this->args.unknown.arg2;
}
```

Since neither `previous_bribing_merchant` nor `merchant_index` change during the loop, the final value of `bribed_councillors` is always either 0 or 4.
This doesn't make any sense as it is, so it is assumed that `bribed_councillors` was intended to be the amount of already bribed councillors in that town, and that the comparison with 2 was intended to prevent a player from bribing the majority of councillors in one town.

## Fix
All bugs are fixed by the [fix-bath-house-bribe-blunders](https://github.com/P3Modding/p3-lib/tree/master/mod-fix-bath-house-bribe-blunders) mod.

### Attribution to Merchant `1`
The councillor's briber must be set to `-1` instead of `1` if the bribe fails and the councillor is not bribed by anyone else.
The original instruction:
```asm
.text:0053AD85                 mov     byte ptr [ecx], 1
```
must be replaced with:
```asm
.text:0053AD85                 mov     byte ptr [ecx], -1
```

### Unforgiving Bath Houses
This cannot be properly fixed easily.
However, resetting the annoyance when opening the bath house is just a small change.
Since the annoyances are reset if the bath house is not opened for 256 ticks, one can replace the conditional jump around the reset code with nops:
```asm
.text:005B17B7 jbe     short loc_5B17CC
```

### Limitless Corruption
This issue is fixed by moving the `previous_bribing_merchant` assignment into the loop and using the loop counter instead of the argument to index the bribes array.

## Footnotes
Since the probability of each councillor appearing is just 7%, you can use the [debug bath house IDC script](https://github.com/P3Modding/p3_ida_scripts) to change it to 100%.
