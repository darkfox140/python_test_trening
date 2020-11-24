from model.contact import NewContact


def test_add_new_contact(app):
    old_contact = app.contact.get_contact_list()
    con = NewContact(first_name="Victor", middle_name="Ivan", last_name="Petrov",
                                              nick_name="Fox140", tittle="test", company="testcompany", address1="Moscow",
                                              home_phone="8(495)2154536", mobile_phone="+79168956384",
                                              work_phone="8-499-9576135", fax="No", email1="testemail1@facegmail.com",
                                              email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",
                                              homepage="testhomepage.ru", bday="14", bmonth="August", byear="1987",
                                              aday="24", amonth="October", ayear="2014", address2="Moscow, Lenina 2",
                                              phone2="8 456 9535956", notes="Test Moscow information")
    app.contact.create_new_contact(con)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(con)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)


'''def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    con = NewContact(first_name="Evgeniy", last_name="Smirnov")
    app.contact.create_new_contact(con)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(con)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)'''