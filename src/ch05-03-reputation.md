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
    + local_donations_rep
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

## Donations
`local_donations_rep` is the merchant's donation reputation in the town.
The donations reputation increases through the following actions:
- Feeding the poor
- Donations (Church)
- Church extension donations
- Granting low interest loans

It decreases through the following actions:
- Bad celebrations

## Trading
TODO

## Buildings
TODO
