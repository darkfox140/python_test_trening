from model.contact import NewContact


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = db.get_contact_list()
    assert sorted(ui_list, key=NewContact.id_or_max) == sorted(db_list, key=NewContact.id_or_max)
