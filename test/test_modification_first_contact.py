from model.contact import NewContact


def test_modification_first_contact_address1(app):
    app.contact.modification_first_contact((NewContact(address1="Omsk, Lenina 2")))
