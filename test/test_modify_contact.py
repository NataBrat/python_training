from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email="New email"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)