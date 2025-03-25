# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact("Ivan", "Ivanov", "Lenina 5","223344", "ivan@test.test"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact(firstname = "", lastname = "", address = "", home_phone = "", email = ""))
    app.session.logout()

