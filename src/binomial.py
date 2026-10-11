def price_european_call(
    spot: float,
    strike: float,
    up_factor: float,
    down_factor: float,
    risk_free_rate: float,
    time_to_expiry: float,
) -> float:
    """Price a European call using a one-step binomial model.

    The risk-free rate is continuously compounded.
    The up/down factors describe the stock's possible price moves.
    """
    if spot <= 0 or strike <= 0:
        raise ValueError("Spot and strike must be positive.")
    if time_to_expiry <= 0:
        raise ValueError("Time to expiry must be positive.")
    if not (0 < down_factor < 1 < up_factor):
        raise ValueError("Require 0 < down_factor < 1 < up_factor.")

    growth = __import__("math").exp(
        risk_free_rate * time_to_expiry
    )

    if not down_factor < growth < up_factor:
        raise ValueError(
            "No-arbitrage condition violated: "
            "down_factor < exp(r*T) < up_factor is required."
        )

    risk_neutral_probability = (
        growth - down_factor
    ) / (up_factor - down_factor)

    up_price = spot * up_factor
    down_price = spot * down_factor

    up_payoff = max(up_price - strike, 0.0)
    down_payoff = max(down_price - strike, 0.0)

    expected_payoff = (
        risk_neutral_probability * up_payoff
        + (1 - risk_neutral_probability) * down_payoff
    )

    return expected_payoff / growth