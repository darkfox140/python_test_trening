from model.contact import NewContact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(nick_name="Железобетон"))
    app.contact.delete_first_contact()
