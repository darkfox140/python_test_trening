from pytest_bdd import given, when, then
from model.contact import NewContact
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <last_name>, <first_name> and <address1>', target_fixture="new_contact")
def new_contact(last_name, first_name, address1):
    return NewContact(last_name=last_name, first_name=first_name, address1=address1)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create_new_contact(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=NewContact.id_or_max) == sorted(new_contacts, key=NewContact.id_or_max)


@given('a non empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_group_list()) == 0:
        app.contact.create_new_contact(NewContact(last_name="test name"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_group(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_group_added(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacs = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacs) - 1 == len(new_contacts)
    old_contacs.remove(random_contact)
    assert old_contacs == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=NewContact.id_or_max) == sorted(app.get_contact_list(), key=NewContact.id_or_max)
