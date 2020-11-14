from model.contact import NewContact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(NewContact(nick_name="Железобетон"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)