# Bath House Bribe Failure
The `handle_operation_bath_house_bribe_failure` function at `0x0053AD10` applies the effects of a failed bribe.

The merchant's social reputation in the corresponding town is decreased by `2.0`.

**If the councillor was already successfully bribed by the merchant or not bribed by any merchant, he will now be bribed by the merchant with the index 1.
This is wrong, as discussed in the Known Bugs chapter.**
