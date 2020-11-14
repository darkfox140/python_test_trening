from model.group import Group


def test_modification_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test name"))
    old_groups = app.group.get_group_list()
    group = Group(name="Клуб")
    group.id = old_groups[0].id
    app.group.modification_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


'''def test_modification_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(header="test header"))
    old_groups = app.group.get_group_list()
    app.group.modification_first_group(Group(header="Участники"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''
