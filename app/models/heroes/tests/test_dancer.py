from ..dancer import Dancer


def test_create_dancer() -> None:
    result = Dancer.create_new()
    assert result.level == 1
