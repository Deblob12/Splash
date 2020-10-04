from config import firebase


class Group:
    def __init__(self, group):
        self.db = firebase.database()
        self.group = group
        self.total = 0
        self.members = []
        self.group_ref = self.db.child('groups').child(self.group)
        self.members_ref = members_ref = self.group_ref.child('members')

    def extract(self, message_body):
        print('From another class')
        self.db.child('members').child(1234567890).child('name').set('John Smith')
        self.db.child('members').child(1234567890).child('Other').set('From the other class')
        return 10

    def venmo_login(self, message_body):
        return None

    def add_member(self, group, number, name):
        self.members_ref.child(str(number)).set({
            'name': name,
            'balance': 0
        })
        self.members.append(number)

    # allocation is a dictionary {name: percent}
    def create_charge(self, group, charge, split_equally, allocation=None):
        count = len(members)
        if count == 0:
            print('Need to add member!')
            return

        self.total += charge

        if split_equally:
            for number in members:
                current = self.members.ref.child(str(number)).child('balance')
                self.members_ref.child(str(number)).update({
                    'balance': current + charge / count
                })

    def push_charges(self, message_body):
        return None

    def end(self, message_body):
        return None
