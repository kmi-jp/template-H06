import types
import pytest

from data.index import Index
from data.series import Series


@pytest.fixture
def users():
    return Index(["user 1", "user 2", "user 3", "user 4"], name="names")


@pytest.fixture
def salaries(users):
    return Series([20000, 300000, 20000, 50000], index=users)


def test_series_get_item(salaries):
    assert salaries["user 2"] == salaries.values[1]

    with pytest.raises(KeyError):
        salaries["wrong key"]


def test_iteration(salaries):
    assert isinstance(salaries.__iter__(), types.GeneratorType)
    assert sum([value for value in salaries]) == sum(salaries.values)


def test_items(users, salaries):
    labels = []
    values = []
    for label, value in salaries.items():
        labels.append(label)
        values.append(value)

    assert isinstance(salaries.items(), zip)

    assert labels == users.labels
    assert values == salaries.values


def test_iterate_over(salaries):
    gen = salaries.iterate_over()

    for i  in range(10):
        assert next(gen) == salaries.values[i % 4]


@pytest.mark.parametrize(
    "function",
    [Series, Series.get, Series.from_csv, Series.shape, Series.items, Series.iterate_over],
)
def test_docstrings(function):
    assert function.__doc__ is not None