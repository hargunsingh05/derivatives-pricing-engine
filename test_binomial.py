from math import exp
from src.binomial import price_european_call

price = price_european_call(
    spot=100,
    strike=100,
    up_factor=1.2,
    down_factor=0.8,
    risk_free_rate=0.05,
    time_to_expiry=1,
)

print(f"European call price: {price:.4f}")

growth = exp(0.05)
p = (growth - 0.8) / (1.2 - 0.8)
expected = (p * 20) / growth

assert abs(price - expected) < 1e-10
print("Test passed!")
