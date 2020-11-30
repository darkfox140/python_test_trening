from model.group import Group
import pytest
# from data.add_group import constant as test_date
from data.add_group import test_date


@pytest.mark.parametrize("group", test_date, ids=[repr(x) for x in test_date])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
