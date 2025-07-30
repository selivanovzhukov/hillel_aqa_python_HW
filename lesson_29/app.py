from db import init_db, insert_user, get_users, update_user, delete_user

if __name__ == "__main__":
    init_db()
    insert_user("Alice")
    print("All users:", get_users())
    update_user(1, "Bob")
    print("Updated users:", get_users())
    delete_user(1)
    print("After delete:", get_users())