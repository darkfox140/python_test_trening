from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(footer="test footer"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
