from model.contact import NewContact


def test_add_new_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(NewContact(first_name="Andrey", middle_name="Ivan", last_name="Maltsev",
                                              nick_name="Fox140", tittle="test", company="testcompany", address1="Moscow",
                                              home_phone="8495*******", mobile_phone="89168******",
                                              work_phone="8499*******", fax="No", email1="testemail1@facegmail.com",
                                              email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",
                                              homepage="testhomepage.ru", bday="14", bmonth="August", byear="1987",
                                              aday="24", amonth="October", ayear="2014", address2="Moscow, Lenina 2",
                                              phone2="Phone2test", notes="Test Moscow information"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)


def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create_empty_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
