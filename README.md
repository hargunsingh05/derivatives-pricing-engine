# Derivatives Pricing Engine

A Python quantitative finance project for pricing European options, estimating risk sensitivities, solving implied volatility, and comparing numerical methods.

## Features

- Black–Scholes pricing for European calls and puts
- One-step and multi-step binomial option pricing
- Cox–Ross–Rubinstein (CRR) binomial tree
- Finite-difference Delta, Gamma, and Vega
- Monte Carlo pricing with standard error and an approximate 95% confidence interval
- Implied volatility estimation using SciPy's Brent root-finding method
- Automated unit tests with pytest
- Pricing comparison CSV and convergence visualisation
- GitHub Actions workflow for automated testing

## Example

For a European call with:

| Parameter | Value |
|---|---:|
| Spot price | 100 |
| Strike price | 100 |
| Risk-free rate | 5% |
| Volatility | 20% |
| Time to maturity | 1 year |

The Black–Scholes benchmark price is approximately **10.450584**.

The numerical experiments compare CRR tree prices at different step counts and Monte Carlo estimates at different simulation counts.

## Reproducibility

Run the project locally using Python and a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

Run the pricing comparison and convergence scripts using the commands defined by the project's source files.

## Validation

The test suite checks pricing results, option sensitivities, implied volatility recovery, and Monte Carlo behaviour. The numerical methods are compared against the Black–Scholes analytical benchmark where appropriate.

## Assumptions and limitations

- The primary pricing models assume European-style exercise.
- Black–Scholes uses constant volatility and a constant risk-free rate.
- The standard binomial and Monte Carlo models use simplifying assumptions about the underlying asset's dynamics.
- Monte Carlo estimates contain sampling error; results can vary between runs.
- Finite-difference Greeks depend on the chosen numerical bump sizes.

These models are educational research implementations, not production trading or investment advice.

## Automated testing

![Python Tests](https://github.com/hargunsingh05/derivatives-pricing-engine/actions/workflows/tests.yml/badge.svg)

Tests run automatically on pushes to `main` and pull requests targeting `main`.

## Tools

Python, NumPy, SciPy, pandas, Matplotlib, and pytest.
