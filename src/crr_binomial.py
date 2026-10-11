from math import exp, sqrt


def crr_price(
    spot: float,
    strike: float,
    rate: float,
    volatility: float,
    maturity: float,
    steps: int,
    option_type: str = "call",
) -> float:
    """Price a European option using the CRR binomial model."""
    if spot <= 0 or strike <= 0:
        raise ValueError("Spot and strike must be positive.")
    if volatility <= 0 or maturity <= 0 or steps < 1:
        raise ValueError("Volatility, maturity and steps must be positive.")
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    dt = maturity / steps
    u = exp(volatility * sqrt(dt))
    d = 1.0 / u
    growth = exp(rate * dt)
    p = (growth - d) / (u - d)

    if not 0 < p < 1:
        raise ValueError("No-arbitrage condition violated.")

    discount = exp(-rate * dt)

    values = []
    for j in range(steps + 1):
        stock = spot * (u ** j) * (d ** (steps - j))
        payoff = (
            max(stock - strike, 0.0)
            if option_type == "call"
            else max(strike - stock, 0.0)
        )
        values.append(payoff)

    for _ in range(steps):
        values = [
            discount * (p * values[j + 1] + (1 - p) * values[j])
            for j in range(len(values) - 1)
        ]

    return values[0]
