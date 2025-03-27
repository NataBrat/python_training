from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_contact(Contact("Oleg", "Ivanov", "Lenina 15", "115599", "ivan@test.test"))