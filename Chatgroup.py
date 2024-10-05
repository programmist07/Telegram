from  Chat import Chat
class Groupchat(Chat):
    def __init__(self, admins):
        self.admin = admins
        self.admins = ["Otabek", "Afruzbek", "Mahsuma"]

    def add_admin(self, user):
        if user not in self.admins:
            self.admins.append(user)
            print(f"{user} yangi admin !!!")
        else:
            print(f"{user} allaqachon admin !!!")

    def remove_admin(self, user):
        if user in self.admins:
            self.admins.remove(user)
            print(f"{user} endi admin emas !!!")

        else:
            print(f"{user} adminlikdan chiqgan !!!")


groupchat = Groupchat("Otabek")
groupchat.add_admin("Otabek")
groupchat.remove_admin("Afruzbek")
