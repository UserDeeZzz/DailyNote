import pytest


class TestCase:

    def test_one(self):
        x = "this"
        assert "h" in x

    @pytest.mark.skip(reason="跳过")
    def test_two(self):
        x = "help"
        assert hasattr(x, "check")

    @staticmethod
    def test_a_list(a_list):
        assert a_list[2] == 4


