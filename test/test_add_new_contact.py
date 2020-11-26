from model.contact import NewContact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    numbers = string.digits
    return "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    email = string.ascii_letters + string.digits
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + ".com"


def random_symbols(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


contact_date = [NewContact(first_name=random_string("First", 10), last_name=random_string("Last", 10),
                           middle_name=random_string("Middle", 10), nick_name=random_string("nick", 10),
                           company=random_string("Company", 20), tittle=random_string("Title", 20),
                           address1=random_symbols("Omskaya", 20), home_phone=random_phone(11),
                           mobile_phone=random_phone(11), work_phone=random_phone(11), fax=random_phone(11),
                           email1=random_email(6), email2=random_email(6), email3=random_email(6),
                           homepage=random_email(8), bday="15", bmonth="May", byear="1978", aday="25", amonth="June",
                           ayear="2007", address2=random_symbols("Lenina", 20), phone2=random_phone(11),
                           notes=random_symbols("Notes", 20))
                for i in range(2)]


@pytest.mark.parametrize("contact", contact_date, ids=[repr(x) for x in contact_date])
def test_add_new_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)
