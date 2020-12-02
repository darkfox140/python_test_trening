from fixture.application import Application
import pytest
import json
import jsonpickle
import os.path
import importlib

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_groups"):
            test_data = load_from_module_groups(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_groups"):
            test_data = load_from_json_groups(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("data_contacts"):
            contact_data = load_from_module_contacts(fixture[5:])
            metafunc.parametrize(fixture, contact_data, ids=[repr(x) for x in contact_data])
        elif fixture.startswith("json_contacts"):
            contact_date = load_from_json_contacts(fixture[5:])
            metafunc.parametrize(fixture, contact_date, ids=[str(x) for x in contact_date])


def load_from_module_groups(module):
    return importlib.import_module("data.%s" % module).test_data


def load_from_json_groups(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_from_module_contacts(module):
    return importlib.import_module("data.%s" % module).contact_data


def load_from_json_contacts(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
