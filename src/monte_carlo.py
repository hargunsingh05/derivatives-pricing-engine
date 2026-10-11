import numpy as np


def monte_carlo_call(
    spot: float,
    strike: float,
    rate: float,
    volatility: float,
    maturity: float,
    simulations: int = 100_000,
    seed: int = 42,
) -> dict[str, float]:
    """Price a European call using risk-neutral Monte Carlo simulation."""

    if spot <= 0 or strike <= 0:
        raise ValueError("Spot and strike must be positive.")
    if volatility < 0 or maturity <= 0:
        raise ValueError("Volatility must be non-negative and maturity positive.")
    if simulations < 2:
        raise ValueError("At least two simulations are required.")

    rng = np.random.default_rng(seed)

    z = rng.standard_normal(simulations)

    terminal_prices = spot * np.exp(
        (rate - 0.5 * volatility**2) * maturity
        + volatility * np.sqrt(maturity) * z
    )

    payoffs = np.maximum(terminal_prices - strike, 0)
    discounted_payoffs = np.exp(-rate * maturity) * payoffs

    price = float(np.mean(discounted_payoffs))
    standard_error = float(
        np.std(discounted_payoffs, ddof=1) / np.sqrt(simulations)
    )

    return {
        "price": price,
        "standard_error": standard_error,
        "ci_95_lower": price - 1.96 * standard_error,
        "ci_95_upper": price + 1.96 * standard_error,
        "simulations": simulations,
    }
