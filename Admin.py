from User import User
class Admin(User):

    users = []
    spam_users = []

    def ban_user(self, user):

        self.spam_users.append(user)
        # self.users.remove(user)
        print(f"Foydalanuvchi {user} ban yeding.")
        with open("admin.txt", "a") as file:
            file.write(f"Foydalanuvchi {user} ban yeding.\n")
    def unban_user(self, user):

        self.users.append(user)
        # self.users.remove(user)
        print(f"Foydalanuvchi {user} ban dan chiqarildi.")
        with open("admin.txt", "a") as file:
            file.write(f"Foydalanuvchi {user} ban dan chiqarildi.\n")

admin = Admin("Ulug'bek", 2, "admin")
admin.unban_user("Ulug'bek")
admin.ban_user("Ulug'bek")
