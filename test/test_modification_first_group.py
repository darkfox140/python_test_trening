from model.group import Group


def test_modification_first_group(app):
    app.group.modification_firtst_group(Group(name="Клуб", header="Участники", footer="Взносы"))
