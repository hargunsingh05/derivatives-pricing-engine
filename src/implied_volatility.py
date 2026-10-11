from scipy.optimize import brentq

from src.black_scholes import black_scholes_price


def implied_volatility(
    market_price: float,
    spot: float,
    strike: float,
    rate: float,
    maturity: float,
    option_type: str = "call",
) -> float:
    """Calculate Black-Scholes implied volatility for a European option."""

    if market_price < 0:
        raise ValueError("Market price cannot be negative.")
    if spot <= 0 or strike <= 0 or maturity <= 0:
        raise ValueError("Spot, strike and maturity must be positive.")
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    def pricing_error(volatility: float) -> float:
        return (
            black_scholes_price(
                spot, strike, rate, volatility, maturity, option_type
            )
            - market_price
        )

    lower_vol = 1e-6
    upper_vol = 5.0

    if pricing_error(lower_vol) * pricing_error(upper_vol) > 0:
        raise ValueError(
            "Market price is outside the solver's volatility bracket."
        )

    return float(brentq(pricing_error, lower_vol, upper_vol))
