# -*- coding: utf-8 -*-
import pytest

from titan.cli import cli_orbit


def cli_orbit_argv(capsys, argv):
    cli_orbit(argv.split())
    out, err = capsys.readouterr()
    assert err == ''
    return out.rstrip()

def test_cli_orbit_date_equinox(capsys):
    assert cli_orbit_argv(capsys, '1980-02-22') == '0.004273686299484325'

def test_cli_orbit_date_equinox_verbose(capsys):
    assert cli_orbit_argv(capsys, '-v 1980-02-22') == u'1980-02-22 -> Ls: 0.00º'


def test_cli_orbit_Ls_equinox(capsys):
    assert cli_orbit_argv(capsys, '0') == '2009-07-30'

def test_cli_orbit_Ls_equinox_verbose(capsys):
    assert cli_orbit_argv(capsys, '-v 0') == u'Ls: 0º (+ 1 Titan year since 1980)-> 2009-07-30'

def test_cli_orbit_Ls_equinox_offset(capsys):
    assert cli_orbit_argv(capsys, '-o 0 0') == '1980-02-22'

def test_cli_orbit_Ls_equinox_offset_verbose(capsys):
    assert cli_orbit_argv(capsys, '-v -o 0 0') == u'Ls: 0º (+ 0 Titan year since 1980)-> 1980-02-22'


def test_cli_orbit_date_multiple(capsys):
    assert cli_orbit_argv(capsys, '2009-07-30 2017-05-14') == '0.004273686299484325\n90.35962529291561'

def test_cli_orbit_Ls_multiple(capsys):
    assert cli_orbit_argv(capsys, '0 10 20 30') == '2009-07-30\n2010-05-21\n2011-03-18\n2012-01-18'


def test_cli_orbit_date_fmt_slash(capsys):
    assert cli_orbit_argv(capsys, '1980/02/22') == '0.004273686299484325'

def test_cli_orbit_date_fmt_datetime(capsys):
    assert cli_orbit_argv(capsys, '1980-02-22T01:02:03') == '0.004273686299484325'


def test_cli_orbit_date_err(capsys):
    with pytest.raises(ValueError):
        cli_orbit_argv(capsys, 'foo')
