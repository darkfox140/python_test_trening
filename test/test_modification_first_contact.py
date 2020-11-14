from model.contact import NewContact


def test_modification_first_contact_address1(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(address1="Тест адресса"))
    old_contact = app.contact.get_contact_list()
    app.contact.modification_first_contact((NewContact(address1="Омск, Ленина 2")))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)


def test_modification_first_contact_birthday(app):
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
    assert len(old_contact) == len(new_contact)
