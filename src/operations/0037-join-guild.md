# Join Guild
The `handle_operation_37_join_guild` at `0x004F8560` checks whether the operation's fee is covered by the merchant's money and whether the merchant is already a member of the guild, and then
- updates the guild membership bitmap of the merchant
- adds the expense to the merchant's bookkeeping
- subtracts the expense from the merchant's money
- adds the entry to the chronicles
- copies the (global) guild expedition disconveries to the merchant's discoveries
- adds the base reputation factor (`1.0` for player merchants) to the local social reputation

The function does not check whether the fee is correct, and no check whether the merchant is the corresponding multiplayer connection's merchant is done.
A malicious client could drain a victim's money by joining a guild at a high price, or save money by joining a guild at a low price.
