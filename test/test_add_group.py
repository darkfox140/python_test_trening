from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="qwerty", header="qazxsw", footer="asdf"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
