from sys import maxsize


class Contact:

    id_or_max = None

    def __init__(self, firstname=None, lastname=None, address=None, home=None, mobile = None, work = None, fax = None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize