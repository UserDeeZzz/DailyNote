import pytest


def f():
    raise SystemExit(1)


def test_r():
    with pytest.raises(SystemExit):
        f()