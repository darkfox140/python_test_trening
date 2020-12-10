from model.contact import NewContact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create_new_contact(NewContact(first_name="Red21", last_name="Gena"))
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="name33", header="headre23"))
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    group_without_contacts = orm.get_groups_not_containing_contact(contact)
    if len(group_without_contacts) == 0:
        app.group.create(Group(name="name45", header="header90"))
        group_without_contacts = orm.get_groups_not_containing_contact(contact)
    group = random.choice(group_without_contacts)
    app.contact.add_contact_to_group_by_id(contact.id, group.id, group.name)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group
