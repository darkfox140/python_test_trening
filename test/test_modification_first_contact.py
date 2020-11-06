# -*- coding: utf-8 -*-
from model.contact import NewContact


def test_modification_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.cotact.modification_empty_contact((NewContact(last_name="Ivan", middle_name="Petr", first_name="Kulik",
                                                      nick_name="red23",tittle="test", company="testcompany",
                                                      address1="Omsk", home_phone="83812*******",
                                                      mobile_phone="89158******", work_phone="83812*******", fax="No",
                                                      email1="testemail1@facegmail.com",
                                                      email2="testemail2@facegmail.com",
                                                      email3="testemail3@facegmail.com",
                                                      homepage="facehomepage.ru", bday="8", bmonth="September",
                                                      byear="1989", aday="7", amonth="May", ayear="2008",
                                                      address2="Omsk, Lenina 2", phone2="Phone2test",
                                                      notes="Test Omsk information")))
    app.session.logout()
