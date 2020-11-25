from model.contact import NewContact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    numbers = string.digits + " "
    return "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


contact_date = [NewContact(first_name=random_string("First", 10), last_name=random_string("Last", 10),
                           middle_name=random_string("Middle", 10), nick_name=random_string("nick", 10),
                           company=random_string("Company", 20), tittle=random_string("Title", 10),
                           address1=random_string("Lenina ", 10), home_phone=random_phone(11),
                           mobile_phone=random_phone(11), work_phone=random_phone(11), fax=random_phone(11))
                for i in range(5)]
"""Доделать завтра весь новый контакт!!!"""


@pytest.mark.parametrize("contact", contact_date, ids=[repr(x) for x in contact_date])
def test_add_new_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)
