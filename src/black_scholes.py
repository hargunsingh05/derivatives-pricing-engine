from math import erf, exp, log, sqrt


def normal_cdf(x: float) -> float:
    """Cumulative distribution function of the standard normal."""
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def black_scholes_price(
    spot: float,
    strike: float,
    risk_free_rate: float,
    volatility: float,
    time_to_expiry: float,
    option_type: str = "call",
) -> float:
    """Price a European call or put on a non-dividend-paying stock."""
    if spot <= 0 or strike <= 0:
        raise ValueError("Spot and strike must be positive.")
    if volatility <= 0 or time_to_expiry <= 0:
        raise ValueError("Volatility and expiry must be positive.")
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    sqrt_t = sqrt(time_to_expiry)
    d1 = (
        log(spot / strike)
        + (risk_free_rate + 0.5 * volatility**2) * time_to_expiry
    ) / (volatility * sqrt_t)
    d2 = d1 - volatility * sqrt_t

    if option_type == "call":
        return (
            spot * normal_cdf(d1)
            - strike * exp(-risk_free_rate * time_to_expiry)
            * normal_cdf(d2)
        )

    return (
        strike * exp(-risk_free_rate * time_to_expiry)
        * normal_cdf(-d2)
        - spot * normal_cdf(-d1)
    )
