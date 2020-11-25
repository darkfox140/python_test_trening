from model.contact import NewContact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdate = [NewContact(first_name="Victor", middle_name="Ivan", last_name="Petrov",
                                              nick_name="Fox140", tittle="test", company="testcompany", address1="Moscow",
                                              home_phone="8(495)2154536", mobile_phone="+79168956384",
                                              work_phone="8-499-9576135", fax="No", email1="testemail1@facegmail.com",
                                              email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",
                                              homepage="testhomepage.ru", bday="14", bmonth="August", byear="1987",
                                              aday="24", amonth="October", ayear="2014", address2="Moscow, Lenina 2",
                                              phone2="8 456 9535956", notes="Test Moscow information")] + [
    NewContact(first_name=random_string("first_name", 10), last_name=random_string("last_name", 10),
               middle_name=random_string("middle_name", 10), company=random_string("company", 20),
               address1=random_string("address1", 20))

    for i in range(5)
]


@pytest.mark.parametrize("contact", testdate, ids=[repr(x) for x in testdate])
def test_add_new_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)


'''def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    con = NewContact(first_name="Evgeniy", last_name="Smirnov")
    app.contact.create_new_contact(con)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(con)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)'''