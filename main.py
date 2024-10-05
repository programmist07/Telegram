class Main:
    def __init__(self):
        self.correct_code = 1111

    def Login(self):
        number = int(input("Telefon raqam kiriting: "))
        print(f"{number} raqamiga kod yuborildi.")
        code = int(input("Kod kiriting: "))
        if code == self.correct_code:
            print("Login muvaffaqiyatli o'tdi!")
            self.Menu()
        else:
            print("Kod noto'g'ri, qaytadan urinib ko'ring.")

    def Menu(self):
        while True:
            print("\n1. User bilan ishlash")
            print("2. Chat bilan ishlash")
            print("3. Guruh chat bilan ishlash")
            print("4. Admin bilan ishlash")
            print("5. Xabarlar bilan ishlash")
            print("0. Chiqish")

            choice = input("Tanlang (0-5): ")
            if choice == '1':
                from User import User

            elif choice == "2":
                from Chat import Chat

            elif choice == '3':
                from Chatgroup import Groupchat

            elif choice == '4':
                from Admin import Admin

            elif choice == '5':
                print("hi")
                from massage import Message

            elif choice == "0":
                break

            else:
                print("Noto'g'ri COMMAND")



if __name__ == "__main__":
    main = Main()
    main.Login()