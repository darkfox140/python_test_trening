from fixture.application import Applicatin
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Applicatin()
    request.addfinalizer(fixture.destroy)
    return fixture
