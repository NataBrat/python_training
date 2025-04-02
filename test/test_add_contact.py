# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact

import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    result = prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])
    # Заменяем двойные пробелы и удаляем пробелы в конце для уменьшения падений теста
    return result.replace("  ", " ").rstrip()

testdata = [Contact(firstname="", lastname="", address="", home="", mobile="",
                    work="", email1="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 10),
            address=random_string("address", 10),
            home=random_string("home", 10),
            mobile=random_string("mobile", 10),
            work=random_string("work", 10),
            email1=random_string("email_1", 10),
            email2=random_string("email_2", 10),
            email3=random_string("email_3", 10))
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
