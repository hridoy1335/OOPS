class tacebook:
    # Constructor
    def __init__(self):
        self.user = ""
        self.password = ""
        self.email = ""
        self.phone = ""
        self.logging = False
        self.menu()
        
    def menu(self):  
        user_input = input("""
                           1. Sign UP
                           2. Sign IN
                           3. Post
                           4. Comment
                           5. Sheare
                           6. Exit
                           => """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        else:
            exit()
            
    def signup(self):
        username = input("Enter your User name => ")
        useremail = input("Enter your User email => ")
        userpassword = input("Setup your User password => ")
        userphone = input("Enter your User phone => ")
        self.user = username
        self.email = useremail
        self.password = userpassword
        self.phone = userphone
        
    def signin(self):
        username = input("Fill the user name => ")
        userpassword = input("Fill the user password => ")
        if username == self.user and userpassword == self.password:
            print("Sign in Successfully.")
            self.logging = True
        else:
            print("Wrong username and password you fill.")        
        
            
user1 = tacebook()