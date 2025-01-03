# Bath House Bribe Success
The `handle_operation_bath_house_bribe_success` function at `0x0053AC50` applies the effects of a successful bribe.
Money is subtracted as expected, and the expenses are added to the monthly expenditure statistic under *"miscellaneous"*.

The merchant's social reputation in the corresponding town is increased as explained in the reputation section.

**There is a check which probably should prevent a merchant from bribing more than 2 councillors in one town. However, this check is bugged, as discussed in the Known Bugs chapter.**
