from config import firebase


class Group:
    def __init__(self, group):
        self.db = firebase.database()
        self.group = group
        self.total = 0
        self.members = []
        self.group_ref = self.db.child('groups').child(self.group)
        self.members_ref = members_ref = self.group_ref.child('members')

    def venmo_login(self, number, name):
        # Log the user in question into Venmo
        # Modify the arguments to pass in other credentials
        return None

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
