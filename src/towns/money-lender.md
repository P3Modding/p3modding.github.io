# Money Lender

## Interest Rates

## Pages

### Grant Loan Page
During every preparation tick of the window the town's loan applications are converted to *grant loan* operations and stored in the window.

### Grant Loan Confirm Page
When the confirm button is clicked and if the merchant has enough money, the selected *grant loan* operation is enqueued.

The interest rate is calculated as follows:
\\[
    f_{setting} * (\sqrt{\frac{1}{\text{weeks} * \text{amount}}} * 300 + 1.2) * 0.1
\\]

where \\(f_{setting}\\) is defined as:

|Setting|Factor|
|||
|Very Low|8|
|Low|9|
|Normal|10|
|High|11|
|Very High|12|

Interest is applied weekly, the repayment sum is capped at 65000.

A loan's success is determined while on the grant loan page and when clicking the interest change buttons on the grant loan confirm page.
The following table defines the safe repayment sums for each debtor's rank:

|Rank|Safe Repayment Sum|
|||
|Shopkeeper|5000|
|Trader|10000|
|Merchant|15000|
|Travelling Merchant|20000|
|Councillor|25000|
|Patrician|30000|

If the repayment sum is bigger than the safe repayment sum, the following computation dedices whether the loan will default:
```c
rand() & 0x3ff < 75 * ((repayment_sum - safe_repayment_sum + 1250) / 1250)
```
