# NetPayCalculator
# Personal Bi-Weekly Net Pay Calculator

A Python script built to solve a real world personal finance problem: accurately predicting take-home pay from hourly wages by simulating payroll tax withholding structures since I got tired of calculating this stuff using online websites

## Features & Logic
* **Time Tracking:** Inputs hours and minutes worked across a two-week pay period.
* **Tax Simulation:** 
  * Deducts pre-tax and post-tax static amounts.
  * Calculates standard OASDI (6.2%) and Medicare (1.45%) employee taxes.
  * Annualizes bi-weekly income to dynamically apply the progressive federal withholding bracket (10% over the $16,100 standard deduction threshold).

## Future Improvements

1. Currently, the minute-to-hourly wage conversion uses a hardcoded rate (`$0.29/min`). I plan to update this to calculate dynamically `(minutes / 60) * pay_hourly` to eliminate compounding rounding errors on larger checks.
2. The current version relies on standard `int(input())`. I plan to implement `try/except` blocks to handle non-numeric inputs gracefully and restrict minutes to values under 60.
3. **Decoupling Data from Logic:** Hardcoded tax rates and pay rates will be moved to a configuration file or environment variables to make the script reusable for others.
