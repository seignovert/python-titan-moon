from datetime import datetime as dt

import numpy as np

from pytest import approx, fixture, raises

from titan import orbit
from titan.orbit import readDate


@fixture
def eq_date():
    """Vernal equinox date."""
    return '1980-02-22'


@fixture
def eq_np_dt():
    """Numpy datetime equinox date."""
    return np.datetime64('1980-02-22', 'D')


@fixture
def cube():
    """Dummy cube with time attribute."""
    class VIMS:
        @property
        def time(self):
            return dt(1980, 2, 22)
    return VIMS()


def test_read_date(eq_np_dt, cube):
    """Test date reader."""
    assert readDate('1980-02-22') == eq_np_dt
    assert readDate('1980-02-22T01:02:03.000') == eq_np_dt
    assert readDate('1980-02-22 01:02:03.000') == eq_np_dt

    assert readDate(dt(1980, 2, 22)) == eq_np_dt
    assert readDate(cube) == eq_np_dt

    assert readDate(eq_np_dt) == eq_np_dt


def test_ls_eq_v(eq_date):
    """Test Ls for the vernal equinox."""
    ls = orbit.Ls(eq_date)
    assert approx(ls, abs=0.05) == 0


def test_date_eq_v(eq_date):
    """Test date for Ls= 0 (vernal equinox)."""
    date = orbit.date(0)
    assert str(date) == eq_date


def test_ls_convergence_err(eq_date):
    """Test invalid date input (limited iteration)."""
    with raises(ValueError):
        orbit.Ls(eq_date, imax=3)
