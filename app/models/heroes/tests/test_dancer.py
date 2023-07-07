from ..dancer import Dancer


def test_create_dancer() -> None:
    result = Dancer.create_new()

    assert result.level == 1
    assert len(result.abilities) == 1
    assert result.abilities[0].name == "Attack"


def test_level_up_dancer() -> None:
    result = Dancer.create_new()

    result.upgrade_to_level(10)
    assert len(result.abilities) == 2
