

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.cotact.delete_first_contact()
    app.session.logout()


def test_delete_all_contact(app):
    app.session.login(username="admin", password="secret")
    app.cotact.delete_all_contact()
    app.session.logout()
