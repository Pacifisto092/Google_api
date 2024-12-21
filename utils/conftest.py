
import pytest

@pytest.fixture(scope="function", autouse=True)
def fixt():
    print("Начало")
    yield
    print("Конец")