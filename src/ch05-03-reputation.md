# Reputation
The function `update_merchant_reputation_and_value` at `0x004F7BB0` calculates the company value and reputation of a given merchant.

Reputation is calculated as follows:
```
reputation = min(0,
    outrigger_rep
    + tenants_rep
    + employment_rep
    + capacity_rep
    + company_value_rep
    + spouse_rep # only in hometown
    + local_social_rep
    + local_trading_rep
    + local_buildings_rep
)
```

## Outrigger
If the merchant is providing the town's outrigger, `outrigger_rep` is set to `1`.

## Tenants
The reputation achieved through tenants is calculated as follows:
```python
def get_tenant_reputation(population_type):
    rent_factor = rent_reputation_factors[rents[population_type]]
    return tenants[population_type] * rent_factor * 0.003

tenants_rep = get_tenant_reputation(rich)
    + get_tenant_reputation(wealthy)
    + get_tenant_reputation(poor)
```

The `rent_reputation_factors` table is at `0x00672DF0`:

|Rent|Reputation Factor|
|-|-|
|None|1.0|
|Low|0.62|
|Normal|0.42|
|High|0.23|
|Very High|0.0|

## Employment
TODO

## Capacity
The merchant's cargo capacity reputation is calculated as follows:
```
capacity_rep = min(5.0, capacity / 100_000.0)
```

## Company Value
The merchant's company value reputation is calculated as follows:
```
company_value_rep = min(5.0, company_value / 100_000.0)
```

## Spouse
Every spouse has a fixed reputation factor.
TODO list options

## Social
`local_social_rep` is the merchant's social reputation in the town.
It is changed through by many actions, and degrades over time.

### Recurring Constants
The following values appear in multiple calculations, and appear to have fixed values.

|Name|Value|Location|
|-|-|-|
|base_rep_factor|1.0|Merchant|
|church_factor|0.0|GameWorld|

### Loans
When granting a loan, `local_social_rep` is increased as follows:
```
local_social_rep += amount / 80_000.0 * interest_factor * base_rep_factor
```
`interest_factor` depends on the chosen interest rate:

|Interest|Factor|
|-|-|
|Very Low|4.0|
|Low|3.0|
|Normal|2.0|
|High|1.0|
|Very High|0.0|

### Church Donations
Donations to the church influence the local social reputation as follows:
```
money_capacity = 12_000 * (church_factor + 1)
effective_amount = min(amount, church_money_capacity - church_money)
local_social_rep += effective_amount
    * 0.0003
    / (church_factor + 1)
    * base_rep_factor
```

### Church Extension Donation
Donations to the church extension influence the local social reputation as follows:
```
effective_amount = min(amount, church_extension_cost - church_extension_money)
local_social_rep += effective_amount
    * 0.0003
    / (church_factor + 1)
    * base_rep_factor
```

### Feeding the Poor
The `handle_feeding_the_poor` function is at `0x004FE557`.
Food donations influence the local social reputation as follows:
```
for amount, ware_id in donation:
    local_social_rep += get_sell_price(ware_id, town_index, amount)
        * 0.0003
        / (church_factor + 1)
        * base_rep_factor
```

### Town Coffers Access

### Celebrations

### Degradation

## Trading
TODO

## Buildings
TODO
