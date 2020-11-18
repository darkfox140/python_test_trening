from model.group import Group
from random import randrange


def test_modification_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test name"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Клуб")
    group.id = old_groups[index].id
    app.group.modification_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


'''def test_modification_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(header="test header"))
    old_groups = app.group.get_group_list()
    app.group.modification_first_group(Group(header="Участники"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''
