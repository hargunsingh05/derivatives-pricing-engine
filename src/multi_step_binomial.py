from math import exp


def price_european_option(
    spot: float,
    strike: float,
    up_factor: float,
    down_factor: float,
    risk_free_rate: float,
    time_to_expiry: float,
    steps: int,
    option_type: str = "call",
) -> float:
    """Price a European option using a multi-step binomial tree."""
    if spot <= 0 or strike <= 0:
        raise ValueError("Spot and strike must be positive.")
    if time_to_expiry <= 0 or steps < 1:
        raise ValueError("Expiry must be positive and steps >= 1.")
    if not (0 < down_factor < 1 < up_factor):
        raise ValueError("Require 0 < down_factor < 1 < up_factor.")
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    dt = time_to_expiry / steps
    growth = exp(risk_free_rate * dt)

    if not down_factor < growth < up_factor:
        raise ValueError("No-arbitrage condition violated.")

    p = (growth - down_factor) / (up_factor - down_factor)

    # Terminal stock prices and option payoffs
    values = []
    for j in range(steps + 1):
        stock = spot * (up_factor ** j) * (
            down_factor ** (steps - j)
        )
        if option_type == "call":
            payoff = max(stock - strike, 0.0)
        else:
            payoff = max(strike - stock, 0.0)
        values.append(payoff)

    # Work backwards through the tree
    discount = exp(-risk_free_rate * dt)
    for _ in range(steps):
        values = [
            discount * (p * values[j + 1] + (1 - p) * values[j])
            for j in range(len(values) - 1)
        ]

    return values[0]