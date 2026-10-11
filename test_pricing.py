from math import exp

import pytest

from src.black_scholes import black_scholes_price
from src.crr_binomial import crr_price


def test_black_scholes_call_benchmark():
    price = black_scholes_price(100, 100, 0.05, 0.20, 1)
    assert price == pytest.approx(10.45058357, abs=1e-7)


def test_black_scholes_put_benchmark():
    price = black_scholes_price(100, 100, 0.05, 0.20, 1, "put")
    assert price == pytest.approx(5.57352602, abs=1e-7)


def test_black_scholes_put_call_parity():
    call = black_scholes_price(100, 100, 0.05, 0.20, 1)
    put = black_scholes_price(100, 100, 0.05, 0.20, 1, "put")
    target = 100 - 100 * exp(-0.05)
    assert call - put == pytest.approx(target, abs=1e-10)


def test_crr_converges_toward_black_scholes():
    exact = black_scholes_price(100, 100, 0.05, 0.20, 1)
    coarse = crr_price(100, 100, 0.05, 0.20, 1, 100)
    fine = crr_price(100, 100, 0.05, 0.20, 1, 500)
    assert abs(fine - exact) < abs(coarse - exact)


def test_invalid_option_type():
    with pytest.raises(ValueError):
        black_scholes_price(100, 100, 0.05, 0.20, 1, "other")
