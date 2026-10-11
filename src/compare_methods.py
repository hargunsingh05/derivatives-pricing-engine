import pandas as pd

from src.black_scholes import black_scholes_price
from src.crr_binomial import crr_price
from src.monte_carlo import monte_carlo_call


def run_comparison():
    spot = 100.0
    strike = 100.0
    rate = 0.05
    volatility = 0.20
    maturity = 1.0

    benchmark = black_scholes_price(
        spot, strike, rate, volatility, maturity
    )

    rows = [{
        "method": "Black-Scholes",
        "price": benchmark,
        "standard_error": 0.0,
    }]

    for steps in [25, 50, 100, 250, 500, 1000]:
        price = crr_price(
            spot, strike, rate, volatility, maturity, steps
        )
        rows.append({
            "method": f"CRR ({steps} steps)",
            "price": price,
            "standard_error": None,
        })

    for simulations in [1000, 10000, 100000, 500000]:
        result = monte_carlo_call(
            spot, strike, rate, volatility, maturity,
            simulations=simulations,
            seed=42,
        )
        rows.append({
            "method": f"Monte Carlo ({simulations} simulations)",
            "price": result["price"],
            "standard_error": result["standard_error"],
        })

    df = pd.DataFrame(rows)
    df["absolute_error"] = (df["price"] - benchmark).abs()
    df["benchmark_price"] = benchmark
    return df


if __name__ == "__main__":
    results = run_comparison()
    print(results.to_string(index=False))
    results.to_csv("results/pricing_comparison.csv", index=False)
    print("Saved results/pricing_comparison.csv")
