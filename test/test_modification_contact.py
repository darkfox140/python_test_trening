from model.contact import NewContact
import random


def test_modification_first_contact_address1(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(first_name="Victor", middle_name="Ivan", last_name="Petrov",
                                              nick_name="Fox140", tittle="test", company="testcompany", address1="Moscow",
                                              home_phone="8(495)2154536", mobile_phone="+79168956384",
                                              work_phone="8-499-9576135", fax="No", email1="testemail1@facegmail.com",
                                              email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",
                                              homepage="testhomepage.ru", bday="14", bmonth="August", byear="1987",
                                              aday="24", amonth="October", ayear="2014", address2="Moscow, Lenina 2",
                                              phone2="8 456 9535956", notes="Test Moscow information"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    mod_contact = NewContact(first_name="Petya", last_name="Petrov")
    app.contact.modification_contact_by_id(contact.id, mod_contact)
    assert len(old_contact) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert len(old_contact) == len(new_contacts)
    if check_ui:
        assert sorted(old_contact, key=NewContact.id_or_max) == \
               sorted(app.group.get_group_list(), key=NewContact.id_or_max)


'''def test_modification_first_contact_birthday(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(bday="01", bmonth="January", byear="2000"))
    old_contact = app.contact.get_contact_list()
    app.contact.modification_first_contact((NewContact(bday="24", bmonth="March", byear="1996")))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)


def test_modification_first_contact_birthday_anniversary(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(bday="01", bmonth="January", byear="2000"))
    old_contact = app.contact.get_contact_list()
    app.contact.modification_first_contact((NewContact(aday="22", amonth="February", ayear="19988")))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)'''
