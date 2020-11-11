from model.group import Group


def test_modification_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test name"))
    app.group.modification_first_group(Group(name="Клуб"))


def test_modification_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(header="test header"))
    app.group.modification_first_group(Group(header="Участники"))
