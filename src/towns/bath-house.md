# Bath House

## Bribes
Every town with a bathhouse has 4 councillors which can be bribed.

### Attendance
Between 0 and 4 bribable councillors attend the bath house.
The bath house panel has an array of attendance selection timestamps at offset `0xd4`, whose entries denote when the attendance in a given town will be updated.
These timestamps are updated to `now + 0x100` when
- the bath house window is closed.
- fast forward is activated.
- the options screen is opened.
- any window is opened after the bath house window has just been closed.

The pool of attending councillors is updated when the bath house window is opened and the selection timestamp is smaller than `now`.
Therefore, continuously opening an individual bath house locks the current attendance.

Attendance is decided as follows:
```python
def will_attend(rand: int):
    return rand % 100 < 7
```
so each councillor has a 7% chance to attend.

### Price Formula
The `town_calculate_expected_bribe` function at `0x00529E20` determines the amount of money the merchant needs to offer for the bribe to be successful.

It defines the following *bribe base factors* for each rank:

|Rank|Bribe Base Factor|
|-|-|
|Shopkeeper|0|
|Trader|1|
|Merchant|2|
|Travelling Merchant|3|
|Councillor|5|
|Patrician|7|
|Mayor|10|
|Alderman|15|

The bribe result is calculated as follows:
```python
BRIBE_BASE_FACTORS = [0, 1, 2, 3, 5, 7, 10, 15]

def calculate_expected_bribe(rank: int, rand: int, already_bribed: bool):
    price = 500 * (rand % 11 + 4 * BRIBE_BASE_FACTORS[rank] + 16)
    if already_bribed:
        price *= 2
    return price

def calculate_bribe_result(amount: int, rank: int, rand: int, already_bribed: bool):
    price = calculcate_expected_bribe(rank, rand, already_bribed)
    if amount < price:
        return BribeResult.OK
    elif amount >= price * 1.5:
        return BribeResult.GOOD
    else:
        return BribeResult.FAILED
```

For unbribed councillors, this produces the following minimum and maximum bribes:

|Rank|Min|Max|
|-|-|-|
|Shopkeeper|8000|13000|
|Trader|10000|15000|
|Merchant|12000|17000|
|Travelling Merchant|14000|19000|
|Councillor|18000|23000|
|Patrician|22000|27000|
|Mayor|28000|33000|
|Alderman|38000|43000|

### Result
The result can be identified by the councillor's response:

|Result|Response|
|-|-|
|Ok|*"Aha, a bribe eh! But all right, I'll take your gold. We'll see what I can do for you at the appointed time."*|
|Good|*"Oh, that's a very enticing sum. You can be certain of my loyalty."*|
|Failed|*"What am I supposed to do with this pittance? You ought to realise yourself, that a man in my position expects a little more from someone of your standing."*|

Both `Ok` and `Good` enqueue a *Bath House Bribe Success* operation, while `Failed` enqueues a *Bath House Bribe Failure* operation.
**The failure operation is bugged, as discussed in the Known Bugs chapter.**

### Status
The current status of a councillor can be inferred by his lines:

|Status|Response|
|-|-|
|Bribed by merchant|*"So we meet again, John Doe. I can very well remember how pleasant our last meeting was."*|
|Bribed by other merchant|*"Ah! You're here as well, John Doe? I have only very recently spoken to one of your competitors."*|
|Not bribed by anyone, annoyed|*"Are you there again?! Let me have my bath in peace, please."*|

**The annoyance of a councillor with a given index is bugged and saved globally, as discussed in the Known Bugs chapter.**

### Limits
The success operation has a check which probably should prevent a merchant from bribing more than 2 councillors in one town.
**However, this check is bugged, as discussed in the Known Bugs chapter.**
