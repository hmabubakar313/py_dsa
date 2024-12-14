class UserDatabase:
    def __init__(self, username, name, email):
        self.user = []
        self.name = name
        self.email = email
        self.username = username


    def insert(self, user):
        i = 0
        while i < len(self.user):
            if self.user[i].username < user.username:
                break
            i += 1
        self.user.insert(i, user)

    def find(self, username):
        for x in len(self.user):
            if username == x.username:
                return x

    def update(self, user):
        username = ''
        target = self.user.find(username)
        target.username, target.email = user.name, user.email

    def list_all(self):
        return self.user

user = UserDatabase()

# aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = UserDatabase('biraj', 'Biraj Das', 'biraj@example.com')
# hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
# jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
# siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
# user.insert(hemanth)
user.insert(biraj)
# user.insert(aakash)
# user.insert(siddhant)
# siddhant = user('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = user('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = user('vishal', 'Vishal Goel', 'vishal@example.com')
