class UsersDAO:

    def __init__(self):
        self.users = []
        U1 = [158, 'Christian', 'Santiago', 7879582355, 'fucksgiven@example.com']
        U2 = [458, 'Rjuan', 'Sanchez', 9394586251, 'givenfucks@example.com']
        U3 = [584, 'Eliemer', 'Velez', 6258849258, 'gifucksven@example.com']
        U4 = [265, 'Superman', 'Kent', 7274567854, 'superman@example.com']
        U5 = [854, 'Batman', 'Wayne', 8002544562, 'bigbat@example.com']
        U6 = [965, 'Batman', 'Kent', 5682541532, 'lilbat@example.com']
        self.users.append(U1)
        self.users.append(U2)
        self.users.append(U3)
        self.users.append(U4)
        self.users.append(U5)
        self.users.append(U6)

    def getUsers(self):
        return self.users

    def getUsersByName(self, name):
        users = []
        for u in self.users:
            if name == u[1]:
                users.append(u)

        return users

    def getUserById(self, usrid):
        users = []
        for u in self.users:
            if usrid == u[0]:
                users.append(u)
        return users

    def getUserByEmail(self, email):
        users = []
        for u in self.users:
            if email == u[4]:
                users.append(u)
        return users

    def getUsersEmails(self):
        emails = []
        for e in self.users:
            emails.append(e)
        return emails
