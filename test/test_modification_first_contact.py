from model.contact import NewContact


def test_modification_first_contact_address1(app):
    app.contact.modification_first_contact((NewContact(address1="Омск, Ленина 2")))


def test_modification_first_contact_birthday(app):
    app.contact.modification_first_contact((NewContact(bday="24", bmonth="March", byear="1996")))


def test_modification_first_contact_birthday_anniversary(app):
    app.contact.modification_first_contact((NewContact(aday="12", amonth="July", ayear="2008")))
