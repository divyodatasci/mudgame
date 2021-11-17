class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.character = ""
        self.score = 0
        self.level=0


'''class LoggedInUser(User):
    def __init__(self, username, password):
        super().__init__(username,password)
        self.character = ""
        self.score = 0
        self.level=0'''
