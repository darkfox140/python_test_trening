# -*- coding: utf-8 -*-
from group import Group
from application import Applicatin
import pytest



@pytest.fixture
def app(request):
    fixture = Applicatin()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="qwerty", header="qazxsw", footer="asdf"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()




