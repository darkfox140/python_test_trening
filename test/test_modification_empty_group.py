# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_empty_group(Group(name="Клуб", header="Участники", footer="Взносы"))
    app.session.logout()