# -*- coding: utf-8 -*-
import pytest

from titan import orbit

EQ_V = '1980-02-22'

def test_Ls_eq_v():
    Ls = orbit.Ls(EQ_V)
    assert pytest.approx(Ls, abs=0.05) == 0

def test_date_eq_v():
    date = orbit.date(0)
    assert str(date) == EQ_V

def test_Ls_convergence_err():
    with pytest.raises(ValueError):
        orbit.Ls(EQ_V, imax=3)