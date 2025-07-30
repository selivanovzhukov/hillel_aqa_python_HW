from db import init_db, insert_user, get_users, update_user, delete_user

def test_crud():
    init_db()
    insert_user("Test")
    users = get_users()
    assert len(users) == 1
    assert users[0][1] == "Test"

    update_user(users[0][0], "Updated")
    assert get_users()[0][1] == "Updated"

    delete_user(users[0][0])
    assert len(get_users()) == 0