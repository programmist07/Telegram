import datetime
class Message:
    def __init__(self, text: str, sender, timestamps):
        self.text = text
        self.sender = sender
        self.timestamps = timestamps

    def get_text(self) -> str:
        return self.text

    def get_sender(self):
        return self.sender

    def get_timestamps(self) -> str:
        return self.timestamps

    def display_message(self) -> str:
        return f"{self.timestamps} - {self.sender}: {self.text}"

vaqt = datetime.datetime.utcnow()
message = Message("Salom, bu xabar!", "Otabek", str(vaqt)[11:16])
print(message.display_message())
