from model.group import Group
import random


def test_modification_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test name"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    mod_group = Group(name="Клуб")
    app.group.modification_group_by_id(group.id, mod_group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


'''def test_modification_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(header="test header"))
    old_groups = app.group.get_group_list()
    app.group.modification_first_group(Group(header="Участники"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''
