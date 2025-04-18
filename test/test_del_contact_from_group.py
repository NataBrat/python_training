from model.contact import Contact
import random
from model.group import Group


def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.user.create(Contact(firstname="Del firstname", lastname="Del lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Del group"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contact_in_group = orm.get_contacts_in_group(group)
    if len(contact_in_group) == 0:
        all_users = orm.get_contact_list()
        contact = random.choice(all_users)
        app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    contact_to_del = random.choice(contacts_in_group)
    app.contact.del_contact_from_group(contact_to_del.id, group.id)
    new_contacts = orm.get_contacts_in_group(group)
    assert contact_to_del not in new_contacts