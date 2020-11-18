from model.contact import NewContact
from random import randrange


def test_modification_first_contact_address1(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(first_name="test"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    cont = NewContact(first_name="Andrey", last_name="Maltsev")
    cont.id = old_contact[index].id
    app.contact.modification_contact_by_index(index, cont)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = cont
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)


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
