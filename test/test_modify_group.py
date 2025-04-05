import random
from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = db.get_group_list()
    group_choice = random.choice(old_groups)
    group = Group(name="New group")
    app.group.modify_group_by_id(group_choice.id, group)
    assert len(old_groups)  == app.group.count()
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_choice)] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#   if app.group.count() == 0:
#        app.group.create(Group(name="test", header="test", footer="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)