from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group( name="yyy", header="ooo", footer="aaa"))
    app.session.logout()