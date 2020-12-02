from model.contact import NewContact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number for contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("simplejson", indent=2)
    out.write(jsonpickle.encode(contact_date))
