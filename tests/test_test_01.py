
import pytest
from test_01.test_01 import test_01 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = test_01()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = test_01(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

