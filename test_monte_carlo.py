import pytest

from src.monte_carlo import monte_carlo_call
from src.black_scholes import black_scholes_price


def test_monte_carlo_is_reproducible():
    first = monte_carlo_call(100, 100, 0.05, 0.20, 1, 10_000, 42)
    second = monte_carlo_call(100, 100, 0.05, 0.20, 1, 10_000, 42)
    assert first == second


def test_confidence_interval_contains_estimate():
    result = monte_carlo_call(100, 100, 0.05, 0.20, 1)
    assert result["ci_95_lower"] <= result["price"]
    assert result["price"] <= result["ci_95_upper"]


def test_standard_error_is_positive():
    result = monte_carlo_call(100, 100, 0.05, 0.20, 1)
    assert result["standard_error"] > 0


def test_estimate_is_reasonably_close_to_black_scholes():
    result = monte_carlo_call(100, 100, 0.05, 0.20, 1)
    benchmark = black_scholes_price(100, 100, 0.05, 0.20, 1)
    assert abs(result["price"] - benchmark) < 0.20


def test_too_few_simulations_are_rejected():
    with pytest.raises(ValueError):
        monte_carlo_call(100, 100, 0.05, 0.20, 1, simulations=1)
