# -*- coding: utf-8 -*-
import pytest
from model.Contact import Contact
from fixture.contact_application import ContactApplication


@pytest.fixture
def app(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username = "admin", password = "secret")
    app.create_contact(Contact("Ivan", "Ivanov", "223344", "ivan@test.test"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username = "admin", password = "secret")
    app.create_contact(Contact(firstname = "", lastname = "", home_phone = "", email = ""))
    app.logout()

