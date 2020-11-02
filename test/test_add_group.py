# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Applicatin
import pytest



@pytest.fixture
def app(request):
    fixture = Applicatin()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qwerty", header="qazxsw", footer="asdf"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
