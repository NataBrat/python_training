# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("Ivan", "Ivanov", "Lenina 5","223344", "ivan@test.test"))



def test_add_empty_contact(app):
    app.contact.create(Contact(firstname = "", lastname = "", address = "", home_phone = "", email = ""))

