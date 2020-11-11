from model.contact import NewContact


def test_modification_first_contact_address1(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(address1="Тест адресса"))
    app.contact.modification_first_contact((NewContact(address1="Омск, Ленина 2")))


def test_modification_first_contact_birthday(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(bday="01", bmonth="January", byear="2000"))
    app.contact.modification_first_contact((NewContact(bday="24", bmonth="March", byear="1996")))


def test_modification_first_contact_birthday_anniversary(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(bday="01", bmonth="January", byear="2000"))
    app.contact.modification_first_contact((NewContact(aday="22", amonth="February", ayear="19988")))
