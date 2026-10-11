from src.black_scholes import black_scholes_price


def calculate_greeks(
    spot: float,
    strike: float,
    rate: float,
    volatility: float,
    maturity: float,
    option_type: str = "call",
    spot_bump: float = 0.01,
    volatility_bump: float = 0.0001,
) -> dict[str, float]:
    """Estimate Delta, Gamma and Vega using finite differences."""
    if spot <= spot_bump or spot_bump <= 0:
        raise ValueError("Spot must exceed a positive spot_bump.")
    if volatility <= volatility_bump or volatility_bump <= 0:
        raise ValueError("Volatility must exceed a positive volatility_bump.")

    def price(s: float, v: float) -> float:
        return black_scholes_price(
            s, strike, rate, v, maturity, option_type
        )

    base = price(spot, volatility)
    up = price(spot + spot_bump, volatility)
    down = price(spot - spot_bump, volatility)

    delta = (up - down) / (2 * spot_bump)
    gamma = (up - 2 * base + down) / (spot_bump ** 2)

    vega = (
        price(spot, volatility + volatility_bump)
        - price(spot, volatility - volatility_bump)
    ) / (2 * volatility_bump)

    return {
        "price": base,
        "delta": delta,
        "gamma": gamma,
        "vega_per_1.00_volatility": vega,
        "vega_per_1_percent": vega * 0.01,
    }
