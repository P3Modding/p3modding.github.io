# Sea Battles

## Sea Battle Struct

## PRNG
Every battle has its own [PRNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) state at offset `0xadc`:
```c
signed __int32 __thiscall get_battle_rand(sea_battle *this)
{
  signed __int32 v1; // edx
  unsigned __int32 v2; // eax
  signed __int32 result; // eax

  v1 = 1153374643 * this->field_ADC_prng_state;
  v2 = -1576685469 - v1;
  this->field_ADC_prng_state = -1576685469 - v1;
  if ( ((99 - (_BYTE)v1) & 1) != 0 )
    result = (v2 >> 1) | 0x80000000;            // shift in a leftmost 1
  else
    result = v2 >> 1;                           // shift in a leftmost 0
  this->field_ADC_prng_state = result;
  return result;
}
```