class User:
    def __init__(self, username, user_id, role):
        self.username = username
        self.user_id = user_id
        self.role = role

    def get_username(self):
        return self.username

    def get_id(self):
        return self.user_id

    def get_role(self):
        return self.role

    def is_admin(self):
        return self.role.lower() == 'admin'


user1 = User("@Afruzbek", 1, "Admin")
user2 = User("@Asadbek", 2, "Foydalanuvchi")
user3 = User("@Humoyun", 3, "Foydalanuvchi")

print(user1.get_username())
print(user1.get_id())
print(user1.get_role())
print(user1.is_admin())

print(user2.get_username())
print(user2.get_id())
print(user2.get_role())
print(user2.is_admin())

print(user3.get_username())
print(user3.get_id())
print(user3.get_role())
print(user3.is_admin())


with open("main.txt", "w+") as file:
    for user in [user1, user2, user3]:
        file.write(f"Username: {user.get_username()}\n\t")
        file.write(f"ID: {user.get_id()}\n\t")
        file.write(f"Role: {user.get_role()}\n\t")
        file.write(f"Is Admin: {user.is_admin()}\n")
