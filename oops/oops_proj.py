"""OOPs Project"""

class ChatBook:
    
    def __init__(self):
        
        self.user_name = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed ?
                           1. Press 1 to signup
                           2. Press 2 to login
                           3. Press 3 to write a post
                           4. Press 4 to message a friend"
                           5. Press any other key to exit
                           """)
        if user_input == '1':
            self.sign_up()

        elif user_input == '2':
            self.sign_in()

        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

        
    def sign_up(self):
        email = input("Enter your Email:- ")
        password = input("Setup your Password:- ")
        self.user_name = email
        self.password = password
        print("You have signed up successfully !!")
        print()
        self.menu()

    def sign_in(self):
        if self.user_name == '' and self.password == '':
            print("Please Signup First by pressing 1 in main menu")
        else:
            uname = input("Enter your Email:- ")
            pwd = input("enter your password here:")
            
            if self.user_name == uname and self.password == pwd:
                print("Login Successful")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        self.menu()

if __name__ == "__main__":
    obj = ChatBook()


    
    