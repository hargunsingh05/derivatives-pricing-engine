# Derivatives Pricing Engine

A Python quantitative finance project for pricing European options, estimating
risk sensitivities, solving implied volatility, and comparing numerical methods.

## Features

- One-step and multi-step binomial pricing
- Black–Scholes European call and put pricing
- Cox–Ross–Rubinstein (CRR) binomial tree
- Finite-difference Delta, Gamma, and Vega
- Monte Carlo pricing with standard error and approximate 95% confidence interval
- Implied volatility using SciPy's Brent root-finding method
- Automated tests with pytest
- Pricing comparison CSV and convergence charts

## Example

For spot = 100, strike = 100, risk-free rate = 5%, volatility = 20%, and
maturity = 1 year, the Black–Scholes European call price is approximately
10.450584.

The comparison experiment evaluates CRR trees at different step counts and
Monte Carlo estimates at different simulation counts.

## Run locally

Use Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pytest -v
python -m src.compare_methods
python -m src.plot_convergence
