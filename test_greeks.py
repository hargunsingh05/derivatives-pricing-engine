import pytest

from src.greeks import calculate_greeks


def test_call_delta_is_between_zero_and_one():
    result = calculate_greeks(100, 100, 0.05, 0.20, 1)
    assert 0 < result["delta"] < 1


def test_call_gamma_is_positive():
    result = calculate_greeks(100, 100, 0.05, 0.20, 1)
    assert result["gamma"] > 0


def test_call_vega_is_positive():
    result = calculate_greeks(100, 100, 0.05, 0.20, 1)
    assert result["vega_per_1.00_volatility"] > 0


def test_put_delta_is_negative():
    result = calculate_greeks(
        100, 100, 0.05, 0.20, 1, option_type="put"
    )
    assert -1 < result["delta"] < 0


def test_invalid_spot_bump_is_rejected():
    with pytest.raises(ValueError):
        calculate_greeks(
            100, 100, 0.05, 0.20, 1, spot_bump=0
        )


def test_invalid_volatility_bump_is_rejected():
    with pytest.raises(ValueError):
        calculate_greeks(
            100, 100, 0.05, 0.20, 1, volatility_bump=0
        )
