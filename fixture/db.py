import pymysql.cursors
from model.group import Group
from model.contact import NewContact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, "
                           "mobile, work, fax, email, email2, email3, homepage, address2, phone2,"
                           "notes from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax,
                 email, email2, email3, homepage, address2, phone2, notes) = row
                list.append(NewContact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname,
                                       nick_name=nickname, company=company, tittle=title, address1=address,
                                       home_phone=home, mobile_phone=mobile, work_phone=work, fax=fax, email1=email,
                                       email2=email2, email3=email3, homepage=homepage, address2=address2,
                                       phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()