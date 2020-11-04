

def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delele_all_group()
    app.session.logout()
