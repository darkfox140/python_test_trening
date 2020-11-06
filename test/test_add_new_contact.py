from model.contact import NewContact


def test_add_new_contact(app):
    app.cotact.create_new_contact(NewContact(last_name="Andrey", middle_name="Ivan", first_name="Maltsev",
                                             nick_name="Fox140",tittle="test", company="testcompany", address1="Moscow",
                                             home_phone="8495*******", mobile_phone="89168******",
                                             work_phone="8499*******", fax="No", email1="testemail1@facegmail.com",
                                             email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",
                                             homepage="testhomepage.ru", bday="14", bmonth="August", byear="1987",
                                             aday="24", amonth="October", ayear="2014", address2="Moscow, Lenina 2",
                                             phone2="Phone2test", notes="Test Moscow information"))


def test_add_empty_contact(app):
    app.cotact.create_empty_contact()