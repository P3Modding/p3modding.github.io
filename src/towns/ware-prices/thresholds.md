# Thresholds
A town's price thresholds are updated by the `update_town_price_thresholds` function at `0x00528070` every time the town ticks.

The calculation is partially understood, but some aspects are still to be determined.
The following pseudocode denotes what is known:
```rust
fn update_town_price_thresholds(town) {
    let mut thresholds = [[0; 4]; 24];
    let mut building_material_factor = 1;
    let mut extra_demand_bitmask = 0;
    let mut t1_days = 14;

    // Consider the town's situation
    if town.flags & (TOWN_FLAG_SIEGE | TOWN_FLAG_BLOCKADE | TOWN_FLAG_PIRATE_ATTACK | TOWN_FLAG_FROZEN) != 0 {
        t1_days = 28;
        building_material_factor = 2;
        extra_demand_bitmask = ware_threshold_bitmask_grain |
            ware_threshold_bitmask_meat |
            ware_threshold_bitmask_fish |
            ware_threshold_bitmask_beer |
            ware_threshold_bitmask_salt |
            ware_threshold_bitmask_honey |
            ware_threshold_bitmask_spices |
            ware_threshold_bitmask_wine |
            ware_threshold_bitmask_timber;
    } else {
        if town.flags & TOWN_FLAG_FIRE != 0 {
            extra_demand_bitmask = ware_threshold_bitmask_grain |
                ware_threshold_bitmask_meat |
                ware_threshold_bitmask_fish |
                ware_threshold_bitmask_beer |
                ware_threshold_bitmask_salt |
                ware_threshold_bitmask_honey |
                ware_threshold_bitmask_spices |
                ware_threshold_bitmask_wine |
                ware_threshold_bitmask_timber;
        } else {
            if town.flags & TOWN_FLAG_FAMINE != 0 {
                extra_demand_bitmask = ware_threshold_bitmask_grain |
                    ware_threshold_bitmask_meat |
                    ware_threshold_bitmask_fish |
                    ware_threshold_bitmask_beer |
                    ware_threshold_bitmask_salt |
                    ware_threshold_bitmask_honey |
                    ware_threshold_bitmask_spices |
                    ware_threshold_bitmask_wine;
            } else if own.flags & TOWN_FLAG_FAMINE != 0 {
                extra_demand_bitmask = ware_threshold_bitmask_grain |
                    ware_threshold_bitmask_meat |
                    ware_threshold_bitmask_fish |
                    ware_threshold_bitmask_beer |
                    ware_threshold_bitmask_salt |
                    ware_threshold_bitmask_honey |
                    ware_threshold_bitmask_spices;
            }
        }
    }

    // Initialize t0 and t1 (for normale wares except bricks)
    for (_, threshold) in thresholds.iter_mut().enumerate().take(19) {
        let t0_days = if extra_demand_bitmask & 1 != 0 { 14 } else { 7 };
        threshold[0] = t0_days;
        threshold[1] = t0_days + t1_days;
        extra_demand_bitmask >>= 1;
    }

    // Initialize t0 and t1 for the rest
    thresholds[WareId::Bricks][0] = 0;
    thresholds[WareId::Brick][1] = 0;
    thresholds[WareId::Sword][0] = 0;
    thresholds[WareId::Sword][1] = 0;
    thresholds[WareId::Bow][0] = 0;
    thresholds[WareId::Bow][1] = 0;
    thresholds[WareId::Crossbow][0] = 0;
    thresholds[WareId::Crossbow][1] = 0;
    thresholds[WareId::Carbine][0] = 0;
    thresholds[WareId::Carbine][1] = 0;

    // Grain t1 bonus
    thresholds[WareId::Grain][1] += t1_days;

    // Scale t0 and t1 with consumption
    for (i, threshold) in thresholds.iter_mut().enumerate().take(20) {
        let consumption = town.consumption_businesses[i]
            + town.consumption_citizens[i]
            + 1;
        threshold[0] *= consumption;
        threshold[1] *= consumption;
    }

    // Siege pitch bonus
    if town.flags & TOWN_FLAG_SIEGE {
        thresholds[WareId::Pitch][0] += 7 * town.get_siege_pitch_consumption();
        thresholds[WareId::Pitch][1] += 14 * town.get_siege_pitch_consumption();
    }

    // Seasonal t1 boni
    match now().month {
        Month::September => { // 0.15
            thresholds[WareId::Grain][1] += thresholds[WareId::Grain][1] * 3 / 20;
            thresholds[WareId::Wine][1] += thresholds[WareId::Wine][1] * 3 / 20;
        }
        Month::October => { // 0.3
            thresholds[WareId::Grain as usize][1] += thresholds[WareId::Grain as usize][1] * 3 / 10;
            thresholds[WareId::Wine as usize][1] += thresholds[WareId::Wine as usize][1] * 3 / 10;
        }
        Month::November => { // 0.2
            thresholds[WareId::Grain as usize][1] += thresholds[WareId::Grain as usize][1] / 5;
            thresholds[WareId::Wine as usize][1] += thresholds[WareId::Wine as usize][1] / 5;
        }
        Month::December => { // 0.1
            thresholds[WareId::Grain as usize][1] += thresholds[WareId::Grain as usize][1] / 10;
            thresholds[WareId::Wine as usize][1] += thresholds[WareId::Wine as usize][1] / 10;
        }
        _ => {}
    }

    // Building material boni
    thresholds[WareId::Pitch][0] += 1800;
    thresholds[WareId::Bricks][0] += 80000 * building_material_factor;
    thresholds[WareId::Timber][0] += 42000;
    thresholds[WareId::Timber][1] += 84000;
    thresholds[WareId::Bricks][1] += 160000 * building_material_factor;
    thresholds[WareId::Pitch][1] += 3600;
    thresholds[WareId::Hemp][0] += 5000 * building_material_factor;
    thresholds[WareId::IronGoods][0] += 2000 * building_material_factor;
    thresholds[WareId::IronGoods][1] += 4000 * building_material_factor;

    /*
    TODO: Weapons
    let mut scaled_citizens = 10 * town.citizens_total / 200;
    if town.flags & (TOWN_FLAG_SIEGE | TOWN_FLAG_PIRATE_ATTACK) != 0 {
        scaled_citizens *= 2;
    }
    */

    // Set t2 and t3 except for bricks and weapons
    for i in 0..19 {
        thresholds[i][2] = thresholds[i][1] + 10 * town.unidentified_array[i];
        thresholds[i][3] = thresholds[i][2] + thresholds[i][0];
    }

    // Pitch and bricks production bonus
    if town.production[WareId::Pitch] > 0 {
        thresholds[WareId::Pitch][3] += 3600;
    }
    if town.production[WareId::Bricks] > 0 {
        thresholds[WareId::Bricks][3] += 160000;
    }

    // Clothes bonus
    thresholds[WareId::Cloth][0] += 400;
    thresholds[WareId::Cloth][1] += 800;
    thresholds[WareId::Cloth][2] += 800;
    thresholds[WareId::Cloth][3] += 1600;

    // Bricks t2 and t3
    if has_effective_bricks_production {
        thresholds[WareId::Bricks][2] = thresholds[WareId::Bricks][1] + town.unidentified_array[WareId::Bricks];
        thresholds[WareId::Bricks][3] = thresholds[WareId::Bricks][1] + 2 * town.unidentified_array[WareId::Bricks];
    } else if thresholds[WareId::Bricks][2] > 2 * thresholds[WareId::Bricks][1] {
        // TODO: can this every be true?
        thresholds[WareId::Bricks][2] = 2 * thresholds[WareId::Bricks][1];
        thresholds[WareId::Bricks][3] = 3 * thresholds[WareId::Bricks][1];
    }

    // Enforce minima
    for (i, threshold) in thresholds.iter_mut().enumerate().take(20) {
        let ware_id = WareId::from_usize(i).unwrap();
        let minimum = if ware_id.is_barrel_ware() {
            1000
        } else {
            10000
        };
        if threshold[0] < minimum {
            threshold[0] = minimum;
        }
        let mut min = minimum + minimum;
        for j in 1..4 {
            if threshold[j] < min {
                threshold[j] = min;
            }
            if threshold[j] <= threshold[j - 1] {
                threshold[j] = threshold[j - 1] + minimum;
            }

            min += minimum;
        }
    }
}
```
