from model.contact import Contact


def test_edit_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_contact(Contact("Oleg", "Ivanov", "Lenina 15", "115599", "ivan@test.test"))
    app.session.logout()