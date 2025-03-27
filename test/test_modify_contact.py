from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New name"))

def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="New email"))