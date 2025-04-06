import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Add group"))
    groups = orm.get_group_list()
    selected_group = random.choice(groups)
    contacts_not_in_group = orm.get_contacts_not_in_group(selected_group)
    if not contacts_not_in_group:
        app.contact.create(Contact(firstname="Add name",lastname="Add lastname"))
        contacts_not_in_group = orm.get_contacts_not_in_group(selected_group)
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact.id, selected_group.id)
    updated_contacts = orm.get_contacts_in_group(selected_group)
    assert contact in updated_contacts