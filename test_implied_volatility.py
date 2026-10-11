import pytest

from src.black_scholes import black_scholes_price
from src.implied_volatility import implied_volatility


def test_recovers_original_call_volatility():
    market_price = black_scholes_price(100, 100, 0.05, 0.20, 1)
    result = implied_volatility(market_price, 100, 100, 0.05, 1)
    assert result == pytest.approx(0.20, abs=1e-8)


def test_recovers_original_put_volatility():
    market_price = black_scholes_price(
        100, 100, 0.05, 0.35, 1, option_type="put"
    )
    result = implied_volatility(
        market_price, 100, 100, 0.05, 1, option_type="put"
    )
    assert result == pytest.approx(0.35, abs=1e-8)


def test_rejects_invalid_option_type():
    with pytest.raises(ValueError):
        implied_volatility(10, 100, 100, 0.05, 1, option_type="invalid")


def test_rejects_negative_market_price():
    with pytest.raises(ValueError):
        implied_volatility(-1, 100, 100, 0.05, 1)


def test_rejects_unattainable_market_price():
    with pytest.raises(ValueError):
        implied_volatility(1000, 100, 100, 0.05, 1)
