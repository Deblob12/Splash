from config import firebase
from venmo_api import Client


class Group:
    def __init__(self, group):
        self.db = firebase.database()
        self.group = group
        self.total = 0
        self.members = []
        self.access_tokens = []
        self.group_ref = self.db.child('groups').child(self.group)
        self.members_ref = members_ref = self.group_ref.child('members')

    def venmo_login(self, number, name, username, password):
        # Log the user in question into Venmo
        # Modify the arguments to pass in other credentials
        access_token = Client.get_access_token(username=username,
                                       password=password)
        self.access_tokens.append((name, number, access_token))

    def add_member(self, number, name):
        self.members_ref.child(str(number)).set({
            'name': name,
            'balance': 0
        })
        self.members.append(number)

    def update_balance(self, number, amount):
        current = self.members_ref.child(str(number)).child('balance')
        self.members_ref.child(str(number)).update({
            'balance': current + amount
        })

    # allocation is a dictionary {name: percent}
    def create_charge(self, charge, split_equally, allocation=None):
        count = len(members)
        if count == 0:
            print('Need to add member!')
            return
        self.total += charge

        if split_equally:
            for number in members:
                self.update_balance(number, charge / count)

    def push_charges(self, message_body):
        all_balances = 0
        for number in self.members:
            all_balances += self.members_ref.chlid(str(number)).child('balance')
        remainder = self.total - all_balances

        r_index = randint(0, len(members))
        self.update_balance(members[r_index], remainder)

        for number in members:
            balance = self.members_ref.child(str(number)).child('balance')
            # Charge venmow with member balance

        return None

    def charge(self, user1, user2, amount):
        accesstoken1 = None
        accesstoken2 = None
        for user in self.access_tokens:
            if user[1] == user1:
                accesstoken1 = user[2]
            elif user[1] == user2:
                accesstoken2 = user[1]
        client1 = Client(accesstoken1)
        client2 = Client(accesstoken2)
        user_id1 = client1.__profile.id
        user_id2 = client2.__profile.id
        if amount > 0:
            client1.payment.request_money(amount, "house expenses", user_id2)
        else:
            client2.payment.request_money(-amount, "house expenses", user_id1)
        

