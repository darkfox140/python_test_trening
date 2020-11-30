from model.contact import NewContact
import random
import string

constant = [
    NewContact(first_name="Victor", middle_name="Ivan", last_name="Petrov", nick_name="Fox140", tittle="test",
               company="testcompany", address1="Moscow", home_phone="8(495)2154536", mobile_phone="+79168956384",
               work_phone="8-499-9576135", fax="85663654556", email1="testemail1@facegmail.com",
               email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",homepage="testhomepage.ru",
               bday="14", bmonth="August", byear="1987", aday="24", amonth="October", ayear="2014",
               address2="Moscow, Lenina 2",phone2="8 456 9535956", notes="Test Moscow information"),
    NewContact(first_name="Gena", middle_name="Kolya", last_name="Smirnov", nick_name="lis144", tittle="testtittle",
               company="testcompany34", address1="Vladimir", home_phone="8(495)4267896", mobile_phone="+79162659698",
               work_phone="8-499-2456247", fax="56575963526", email1="teste23mail1@facegmail.com",
               email2="testemail2456@facegmail.com", email3="testemail3453@facegmail.com", homepage="testhomepage4.ru",
               bday="15", bmonth="August", byear="1988", aday="25", amonth="October", ayear="2012",
               address2="Omsk, Lenina 2",phone2="8 456 9535956", notes="Test Omsk information")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    numbers = string.digits
    return "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    email = string.ascii_letters + string.digits
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + ".com"


def random_symbols(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


contact_date = [NewContact(first_name=random_string("First", 10), last_name=random_string("Last", 10),
                           middle_name=random_string("Middle", 10), nick_name=random_string("nick", 10),
                           company=random_string("Company", 20), tittle=random_string("Title", 20),
                           address1=random_symbols("Omskaya", 20), home_phone=random_phone(11),
                           mobile_phone=random_phone(11), work_phone=random_phone(11), fax=random_phone(11),
                           email1=random_email(6), email2=random_email(6), email3=random_email(6),
                           homepage=random_email(8), bday="15", bmonth="May", byear="1978", aday="25", amonth="June",
                           ayear="2007", address2=random_symbols("Lenina", 20), phone2=random_phone(11),
                           notes=random_symbols("Notes", 20))
                for i in range(2)]
