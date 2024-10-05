class Chat:
    def __init__(self, users, messages, chat_id):
        self.users = users
        self.messages = messages
        self.chat_id = chat_id

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self):
        self.messages.pop(self.users)

    def add_message(self, message):
        self.messages.append(message)
        # return messages

        with open("chat.txt", "a") as file:
            file.write(f"Xabarlar: {message}\n\n")
            return message

    def get_chat_history(self):
        # return self.messages

        with open("chat.txt", "r") as file:
            data = file.read()
            return data


users = ["Mahsuma", "Madina"]
messages = []
a = Chat(users, messages, 6)


print(a.add_message("Madina, please read my message on IELTS Generation group"))
print(a.get_chat_history())