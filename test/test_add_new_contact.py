from model.contact import NewContact
import pytest
from data.add_new_contact import contact_date


@pytest.mark.parametrize("contact", contact_date, ids=[repr(x) for x in contact_date])
def test_add_new_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=NewContact.id_or_max) == sorted(new_contact, key=NewContact.id_or_max)
