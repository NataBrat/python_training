from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    app.contact.modify_first_contact(Contact(firstname="New name"))

def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(email="New email"))